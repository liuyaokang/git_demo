def parase_list(url):
    next_page = 1
    tabid = 0
    total_page =1
    page_size =15
    o = urlparse(url)
    query_dict = parse_qs(o.query)
    cate_id = query_dict["category"][0]

    category_rsp = requests.get(url)
    if category_rsp.status_code !=200:
        raise Exception('反爬了')

    data = re.search('(?<= (window.__INITIAL_STATE__=)).* ?(?=(;</script>))',category_rsp.text,re.IGNORECASE)
    #re.IGNORECASE忽略大小写
    if data:
        data_str =data.group()
        data_json = json.loads(data_str)
        data_list = data_json["pageData"]["data"]["baseInfo"]["dataList"]
    extract_topic(data_json["pageData"]["data"]["baseInfo"]["dataList"])
    return data