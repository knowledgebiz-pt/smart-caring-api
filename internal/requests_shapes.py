import requests
import json


def login_shapes():
    url = "https://kubernetes.pasiphae.eu/shapes/marketplace-backend/auth/login"

    payload = json.dumps({
        "email": "oscar.silva@knowledgebiz.pt",
        "password": "Development@2023"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_json = response.json()

    print(response_json["data"]["items"][0]["token"])

    return response_json["data"]["items"][0]["token"]


def get_all_products():

    token = login_shapes()

    url = "https://kubernetes.pasiphae.eu/shapes/marketplace-backend/products/all"

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response_json = response.json()

    return response_json

