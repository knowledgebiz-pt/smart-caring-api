import bson.objectid
from mongoengine import connect
import core.models as model
import json

import core.models.likes_model

#CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'
CONNECTION = 'mongodb://localhost:27017/smartcaring?retryWrites=true&w=majority'
connect(host='mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority')
def test_add_like():
    value = {
        "is_like": True,
        "user_id": "12345",
        "news_id": "645bb9f4fb5e071940871259"
    }

    response = model.likes_model.Likes(
        is_like = value["is_like"],
        user_id = value["user_id"],
        news_id = value["news_id"]
    ).save()
    assert type(response.auto_id_0) == bson.objectid.ObjectId

def test_return_likes_by_news_id():
    connect(host=CONNECTION)
    id_news = "645bb9f4fb5e071940871259"
    response = model.likes_model.Likes.objects(news_id=id_news)
    response = json.loads(response.to_json()) if response is not None else None
    assert type(response["_id"]) == bson.objectid.ObjectId

def test_return_likes_by_user_id():
    connect(host=CONNECTION)
    id_user = "12345"
    response = model.likes_model.Likes.objects(user_id=id_user)
    response = json.loads(response.to_json()) if response is not None else None
    assert type(response["_id"]) == bson.objectid.ObjectId

def test_delete_like_by_id():
    id_like = "645bc066c76b21b3d5b83492"
    connect(host=CONNECTION)
    response = model.likes_model.Likes.objects(_id=id_like)
    response.delete()
    assert response["msg"] == "success"