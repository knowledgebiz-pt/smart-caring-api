import datetime

from mongoengine import connect
import pymongo
import core.models as model
import json
import core.models.news_model


CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'
#CONNECTION = 'mongodb://localhost:27017/smartcaring?retryWrites=true&w=majority'


def add_news(value):
    """
    Create new news article in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    content = core.models.news_model.ModelContent()
    content.type = value.content.type
    content.path = value.content.path

    response = model.news_model.News(
        user_id=value.user_id,
        text=value.text,
        content=content,
        link=value.link,
        likes=value.likes,
        favorites=value.favorites,
        date=str(datetime.datetime.now()),
    ).save()
    return str(response.auto_id_0)


def return_news_by_id(id_news):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id=id_news).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_news_by_user_id(id_user):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(user_id=id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_all_news():
    connect(host=CONNECTION)
    response = model.news_model.News.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def delete_news_by_id(id_news):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id=id_news)
    response.delete()
    return response


def add_like_in_news(id_news, id_user):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id=id_news).update_one(push__likes=id_user)
    return response


def delete_like_in_news(id_news, id_user):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id=id_news).update_one(pull__likes=id_user)
    return response


def add_favorite_in_news(id_news, id_user):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id=id_news).update_one(push__favorites=id_user)
    return response


def delete_favorite_in_news(id_news, id_user):
    connect(host=CONNECTION)
    response = model.news_model.News.objects(_id=id_news).update_one(pull__favorites=id_user)
    return response
