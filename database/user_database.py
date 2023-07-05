import os
from mongoengine import connect
import core.models as model
import string
import json
import random
from datetime import datetime
import core.models.user_model
import internal

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'

connect(host='mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority')


def add_user(value):
    """
    Create new user in database
    :param value:
    :return:
    """

    address = core.models.user_model.ModelUserAddress()
    address.city = value.address.city
    address.street = value.address.street
    address.country = value.address.country
    address.door_number = value.address.door_number
    address.postal_code = value.address.postal_code

    response = model.user_model.User(
        name=value.name,
        email=value.email.lower(),
        user_gender=value.user_gender,
        user_type=value.user_type,
        visibility=value.visibility,
        receives_notification=value.receives_notification,
        notification_email=value.notification_email,
        password=value.password,
        picture=value.picture,
        phone=value.phone,
        birth_date=value.birth_date,
        gmail_access_token=value.gmail_access_token,
        exponent_push_token=value.exponent_push_token,
        address=address
    )#.save()
    if (internal.validate_password.password_check(value.password)):
        response.save()
        response_status = "Success"
        return str(response.auto_id_0)
    else:
        response_status = "Invalid Password. Password must contain a minimun of 8 digits, a uppercase and lowercase letter, a digit and a special character"
        return str(response_status)



def return_user_by_email_and_password(email, password):

    response = model.user_model.User.objects(email=email, password=password).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_user_by_email(email):

    response = model.user_model.User.objects(email=email).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_all_users():

    response = model.user_model.User.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response

import secrets


def add_recover_password(value):
    code_generate = str(random.randint(1000, 9999))
    response = model.user_model.ForgotPassword(
        user_email=value["email"].lower(),
        code=code_generate,
        created=str(datetime.now())
    ).save()
    internal.send_email.send_recovery_code(value, code_generate)
    return str(response.auto_id_0)


def return_verify_email_and_code(user_email, code):

    response = model.user_model.ForgotPassword.objects(user_email=user_email, code=code).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def update_user_password(email, password):

    response = model.user_model.User.objects(email=email)
    response_update = response.update(password=password)
    if response_update == 1:
        return True
    else:
        return False


