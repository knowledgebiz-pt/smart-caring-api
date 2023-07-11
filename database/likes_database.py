import core.models as model
import json
import core.models.likes_model
import os
from mongoengine import connect

connect(host=os.getenv('DATABASE_CONNECTION'))


def add_like(value):
    """
    Create new like in database
    :param value:
    :return:
    """
    response = model.likes_model.Likes(
        is_like = value.is_like,
        user_id = value.user_id,
        news_id = value.news_id
    ).save()
    return str(response.auto_id_0)


def return_likes_by_id_news(id_news):

    response = model.likes_model.Likes.objects(news_id = id_news)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_likes_by_user_id(id_user):

    response = model.likes_model.Likes.objects(user_id = id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def delete_likes_by_id(id_likes):

    response = model.likes_model.Likes.objects(_id = id_likes)
    response.delete()
    return response