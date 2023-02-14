from modles import Topic
from datetime import datetime
def extract_topic(data_list):
    for value in data_list:
        # 解析user和topic入库
        content = value["content"]
        topic = Topic()
        topic.id = content["contentId"]
        topic.title = content["topicTitle"]
        topic.content = content["description"]
        topic.create_time = datetime.strptime(content["createTime"], '%Y-%m-%d %H:%M:%S')
        # topic.create_time = datetime.strptime(content["createTime"], '%Y-%m-%d %H:%M:%S')
        topic.answer_nums = content["commentCount"]
        topic.click_nums = content["viewCount"]
        topic.praised_nums = content["diggNum"]
        topic.author = content["username"]

        topic.save()
        # pass
        existed_topics = Topic.select().where(Topic.id == topic.id)
        if existed_topics:
            topic.save()
        else:
            topic.save(force_insert=True)
        # parse_topic(content["url"])
