from mongoengine import connect
import datetime
import core.models as model
import json
import os


connect(host=os.getenv('DATABASE_CONNECTION'))


def add_comment(value):
    """
    Create new comment in database
    :param value:
    :return:
    """

    response = model.comment_model.Comment(
        news_id = value.news_id,
        comment_reply_id = value.comment_reply_id,
        user_id = value.user_id,
        text = value.text,
        link = value.link,
        likes = value.likes,
        date = str(datetime.datetime.now()),
    ).save()
    return str(response.auto_id_0)

def return_comments_by_id(id_comment):

    response = model.comment_model.Comment.objects(_id = id_comment)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_comments_by_id_news(id_news):

    response = model.comment_model.Comment.objects(news_id = id_news)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_comments_by_user_id(id_user):

    response = model.comment_model.Comment.objects(user_id = id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def delete_comment_by_id(id_comment):

    response = model.comment_model.Comment.objects(_id = id_comment)
    response.delete()
    return response

def delete_comments_by_id_news(id_news):

    response = model.comment_model.Comment.objects(news_id = id_news)
    response.delete()
    return response