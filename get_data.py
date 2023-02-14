import re
import json
from urllib.parse import urlparse,parse_qs
from save_topic import extract_topic
import requests
from get_urls import get_last_urls

def parase_list(url):

    # next_page = 1
    # tabid = 0
    # total_page =1
    # page_size =15
    # o = urlparse(url)
    # query_dict = parse_qs(o.query)
    # cate_id = query_dict["category"][0]
    #
    category_rsp = requests.get(url)
    if category_rsp.status_code !=200:
        raise Exception('反爬了')
    r = category_rsp.text
    data = re.search('window.__INITIAL_STATE__=(.*}});</script>', category_rsp.text, re.IGNORECASE)
    # data = re.search('(?<= (window.__INITIAL_STATE__=)).* ?(?=(;</script>))',category_rsp.text,re.IGNORECASE)
    #re.IGNORECASE忽略大小写
    if data:
        data_str =data.group(1)
        data_json = json.loads(data_str)
        data_list = data_json["pageData"]["data"]["baseInfo"]["dataList"]
    extract_topic(data_json["pageData"]["data"]["baseInfo"]["dataList"])
    # return data


if __name__ == "__main__":
    urls = get_last_urls()
    for url in urls:
        parase_list(url)
        break
    # parase_list('https://bbs.csdn.net/forums/wfuw?category=307570')