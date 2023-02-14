from modles import Topic,Answer,Author
from datetime import datetime


def extract_topic(data_list):
    for value in data_list:
        # 解析user和topic入库
        content = value["content"]
        topic = Topic()
        topic.id = content["contentId"]
        topic.title = content["topicTitle"]
        topic.content = content['description']
        if topic.content == None:
            topic.content = '暂无数据'
        topic.last_answer_time = datetime.strptime(content['updateTime'], '%Y-%m-%d %H:%M:%S')
        topic.create_time = datetime.strptime(content["createTime"], '%Y-%m-%d %H:%M:%S')
        topic.answer_nums = content["commentCount"]
        topic.click_nums = content["viewCount"]
        topic.praised_nums = content["diggNum"]
        topic.author = content["username"]

        existed_topics = Topic.select().where(Topic.id == topic.id)
        if existed_topics:
            topic.save()
        else:
            topic.save(force_insert=True)
        pass
        # parse_topic(content["url"])
        # parse_author(f'https://blog.csdn.net/{content["username"]}')