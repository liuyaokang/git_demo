import re
import json
from urllib.parse import urlparse, parse_qs
from csdn import Signer

from saveto_db.save_topic import extract_topic
import requests
from get_urls import get_last_urls

def parse_list(url):
    #获取分类下的category列表
    cagetory_rsp = requests.get(url)
    if cagetory_rsp.status_code != 200:
        raise Exception("反爬了")
    data = re.search('window.__INITIAL_STATE__=(.*}});</script>', cagetory_rsp.text, re.IGNORECASE)
    from urllib.parse import urlparse, parse_qs

    o = urlparse(url)
    query = parse_qs(o.query)
    cate_id = query["category"][0]
    next_page = 1
    page_size = 15
    tabid = 0
    total_pages = 1
    if data:
        data = data.group(1)
        data = json.loads(data)
        total = data["pageData"]["data"]["baseInfo"]["page"]["total"]
        tabid = data["pageData"]["data"]["baseInfo"]["defaultActiveTab"]
        total_pages = total / page_size
        if total % page_size > 0:
            total_pages += 1
        extract_topic(data["pageData"]["data"]["baseInfo"]["dataList"])
        # next_page = current_page + 1

    # while next_page < total_pages:
    #     #注意这里的参数顺序，一定要按照ascii编码排序！！！！！
    #     url = f"https://bizapi.csdn.net/community-cloud/v1/community/listV2?communityId={cate_id}&noMore=false&page={next_page}&pageSize={page_size}&tabId={tabid}&type=1&viewType=0"
    #     signer = Signer()
    #     code, re_json = signer.get_html(url)
    #     if code != 200:
    #         raise Exception("获取下一页反爬了")
    #     extract_topic(re_json["data"]["dataList"])

if __name__ == '__main__':
    urls = get_last_urls()
    for url in urls:
        parse_list(url)
    # parase_list('https://bbs.csdn.net/forums/wfuw?category=307570')