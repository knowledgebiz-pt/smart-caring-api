import bson.objectid
from mongoengine import connect
import core.models as model
import json

import core.models.news_model

#CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'
CONNECTION = 'mongodb://localhost:27017/smartcaring?retryWrites=true&w=majority'
connect(host='mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority')

def test_add_news():
    value = {
        "title": "PytestDatabase",
        "content": "sjakhdfauibfveqihvdsgbwjvkdlsnvjikcxbvuhrwqsaldbvuihwbfd vqiodjavbjkhewdbvjiewqbfviwqe",
        "user_id": "12345",
        "picture": "",
        "video": ""
    }

    response = model.news_model.News(
        title = value["title"],
        content = value["content"],
        user_id = value["user_id"],
        picture = value["picture"],
        video = value["video"],
    ).save()
    assert type(response.auto_id_0) == bson.objectid.ObjectId

def test_return_news_by_id():

    #id_news = "645bb9c9955f519614360419"
    id_news = "646b25481595a6384092a3f9"
    response = model.news_model.News.objects(_id=id_news)
    response = json.loads(response.to_json()) if response is not None else None
    assert type(response["_id"]) == bson.objectid.ObjectId

def test_return_news_by_user_id():

    id_user = "12345"
    response = model.news_model.News.objects(user_id=id_user)
    response = json.loads(response.to_json()) if response is not None else None
    print(response)
    assert type(response["_id"]) == bson.objectid.ObjectId

def test_delete_news_by_id():
    id_news = "645bc066c76b21b3d5b83492"

    response = model.news_model.News.objects(_id=id_news)
    response.delete()
    assert response["msg"] == "success"