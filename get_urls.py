import requests
from scrapy import Selector #使用scrapy的Selector解析html

from csdn import Signer


def get_last_urls():
    urls = []
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    }
    rsp = requests.get("https://bbs.csdn.net/forums/activity",headers=headers)
    if rsp.status_code !=200:
        raise Exception("反爬了")
    '''获取社区一级目录下的html'''
    sel = Selector(text=rsp.text)
    c_nodes = sel.css("div.custom-tree-node")

    '''css选择器去识别定位到url相关的的节点'''

    for index,c_node in enumerate(c_nodes):
        url = "https://bizapi.csdn.net/community-cloud/v1/homepage/community/by/tag?deviceType=PC&tagId={}".format(index+1)
        '''一级目录的url'''
        singer = Signer()
        code,re_json = singer.get_html(url)
        if code!=200:
            raise Exception("反爬了")
        '''根据singer中的反反爬函数去抓取一级页面的数据，取一级目录下二级目录的'''
        if  "data" in re_json:
            for item in re_json["data"]:
                url = "{}?category={}".format(item['url'],item['id'])
                urls.append(url)
        break
    return urls

if __name__ == "__main__":
    urls=get_last_urls()
