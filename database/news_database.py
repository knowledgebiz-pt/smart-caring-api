from mongoengine import connect
import core.models as model
import json

import core.models.news_model

#CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'
CONNECTION = 'mongodb://localhost:27017/smartcaring?retryWrites=true&w=majority'

def add_news(value):
    """
    Create new news article in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.news_model.News(
        title = value.title,
        content = value.content,
        user_id = value.user_id,
        picture = value.picture,
        video = value.video,
    ).save()
    return str(response.auto_id_0)


def return_news_by_id(id_news):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id = id_news)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_news_by_user_id(id_user):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(user_id = id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def delete_news_by_id(id_news):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id = id_news)
    response.delete()
    return response