from mongoengine import connect
import core.models as model
import json
import random
from datetime import datetime
import core.models.user_model

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'


def add_user(value):
    """
    Create new user in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    address = core.models.user_model.ModelUserAddress()
    address.city = value.address.city
    address.street = value.address.street
    address.country = value.address.country
    address.door_number = value.address.door_number
    address.postal_code = value.address.postal_code

    response = model.user_model.User(
        name=value.name,
        email=value.email,
        user_gender=value.user_gender,
        user_type=value.user_type,
        receives_notification=value.receives_notification,
        notification_email=value.notification_email,
        password=value.password,
        picture=value.picture,
        phone=value.phone,
        birth_date=value.birth_date,
        gmail_access_token=value.gmail_access_token,
        exponent_push_token=value.exponent_push_token,
        address=address
    ).save()
    return str(response.auto_id_0)


def return_user_by_email_and_password(email, password):
    connect(host=CONNECTION)
    response = model.user_model.User.objects(email=email, password=password).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_user_by_email(email):
    connect(host=CONNECTION)
    response = model.user_model.User.objects(email=email).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def add_recover_password(value):
    response = model.user_model.ForgotPassword(
        user_email=value["email"],
        code=random.randint(000000, 999999),
        created=str(datetime.now())
    ).save()
    return str(response.auto_id_0)


def return_verify_email_and_code(user_email, code):
    connect(host=CONNECTION)
    response = model.user_model.ForgotPassword.objects(user_email=user_email, code=code).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def update_user_password(email, password):
    connect(host=CONNECTION)
    response = model.user_model.User.objects(email=email)
    response_update = response.update(password=password)
    if response_update == 1:
        return True
    else:
        return False


