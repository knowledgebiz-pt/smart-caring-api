import json
import internal
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
prefix = "likes"

def test_get_all_user_likes():
    end_point = "by-user-id"
    test_id = "12345"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list

def test_get_all_user_likes_error():
    end_point = "by-user-id"
    test_id = "fakeid"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["msg"] == "error"
    assert type(response_json["data"]) == str

def test_get_likes_by_news_id():
    end_point = "by-news-id"
    test_id = "645bb9c9955f519614360419"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    print(path)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list

def test_get_article_by_id_error():
    end_point = "by-id"
    test_id = "111111111111111111111111"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    print(path)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json["msg"] == "error"
    assert type(response_json["data"]) == str

def test_create_like():
    path = f"/{prefix}/".format(prefix=prefix)
    body = {
        "is_like": True,
        "user_id": "12345",
        "news_id": "645bb9c9955f519614360419",
    }
    response = client.post(path,json=body)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list

def test_create_like_error():
    path = f"/{prefix}/".format(prefix=prefix)
    body = {
        "user_id": "12345",
        "news_id": ""
    }
    response = client.post(path, json=body)
    response_json = response.json()
    assert response.status_code == 422

def test_delete_like():
    end_point = "by-id"
    test_id = "645bb9f4fb5e071940871259"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.delete(path)
    response = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == list