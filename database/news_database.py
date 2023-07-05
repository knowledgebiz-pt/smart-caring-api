import datetime
import uuid
from mongoengine import connect
import core.models as model
import json
import core.models.news_model
import internal.connection_azure_storage
import os
from mongoengine import connect
import os


connect(host=os.getenv('DATABASE_CONNECTION'))


def add_news(value):
    """
    Create new news article in database
    :param value:
    :return:
    """

    content = core.models.news_model.ModelContent()
    content.type = value.content.type
    content.path = value.content.path

    content_file = None

    if len(content.path) > 100:
        content_file = internal.connection_azure_storage.upload_image(value.content.path, str(uuid.uuid4()),
                                                                      value.content.type)
        content.path = content_file

        if content_file is None:
            return None

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

    response = model.news_model.News.objects(_id=id_news).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_news_by_user_id(id_user):

    response = model.news_model.News.objects(user_id=id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_all_news():

    response = model.news_model.News.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def delete_news_by_id(id_news):

    response = model.news_model.News.objects(_id=id_news)
    response.delete()
    return response


def add_like_in_news(id_news, id_user):

    response = model.news_model.News.objects(_id=id_news).update_one(push__likes=id_user)
    return response


def delete_like_in_news(id_news, id_user):

    response = model.news_model.News.objects(_id=id_news).update_one(pull__likes=id_user)
    return response


def add_favorite_in_news(id_news, id_user):

    response = model.news_model.News.objects(_id=id_news).update_one(push__favorites=id_user)
    return response


def delete_favorite_in_news(id_news, id_user):

    response = model.news_model.News.objects(_id=id_news).update_one(pull__favorites=id_user)
    return response
