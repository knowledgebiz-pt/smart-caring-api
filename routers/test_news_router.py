import json
import internal
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
prefix = "news"

def test_get_all_user_news():
    end_point = "by-user-id"
    test_id = "12345"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list

def test_get_all_user_news_error():
    end_point = "by-user-id"
    test_id = "fakeid"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["msg"] == "error"
    assert type(response_json["data"]) == str

def test_get_article_by_id():
    end_point = "by-id"
    test_id = "645bb9c9955f519614360419"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list

def test_get_article_by_id_error():
    end_point = "by-id"
    test_id = "111111111111111111111111"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["msg"] == "error"
    assert type(response_json["data"]) == str

def test_create_article():
    path = f"/{prefix}/".format(prefix=prefix)
    body = {
        "title": "PytestArticle",
        "content": "Content is more than fifty characters, less than three thousand.",
        "user_id": "12345",
        "picture": "",
        "video": ""
    }
    response = client.post(path,json=body)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list

def test_create_article_length_error():
    path = f"/{prefix}/".format(prefix=prefix)
    body = {
        "title": "PytestArticle",
        "content": "Content is less than fifty characters",
        "user_id": "12345",
        "picture": "",
        "video": ""
    }
    response = client.post(path, json=body)
    response_json = response.json()
    assert response.status_code == 422

def test_create_article_missing_field():
    path = f"/{prefix}/".format(prefix=prefix)
    body = {
        "content": "Content is over fifty characters - abcdefghhijkjsadkosajckxznfbwqiebwqrxzcfa",
        "user_id": "12345",
        "picture": "",
        "video": ""
    }
    response = client.post(path, json=body)
    response_json = response.json()
    assert response.status_code == 422

def test_delete_article():
    end_point = "by-id"
    test_id = "645bb9f4fb5e071940871259"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.delete(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list