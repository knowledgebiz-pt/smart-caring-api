import pytest
from database import user_database
import core.schemes as model
from fastapi.encoders import jsonable_encoder
import os
from mongoengine import connect


connect(host=os.getenv('DATABASE_CONNECTION'))



def create_user_address_data():
    address = model.user_schemes.UserAddress
    address.city = "city"
    address.street = "street"
    address.country = "country"
    address.postal_code = "2222222"
    address.door_number = "1J"
    return address


def create_user_data():
    user = model.user_schemes.UserPost
    user.name = "oscar"
    user.email = "testeemail.pt"
    user.receives_notification = False
    user.notification_email = "test.notifications@email.pt"
    user.password = "test.password1234"
    user.picture = "image.png"
    user.phone = "999999999"
    user.birth_date = "01-01-2000"
    user.gmail_access_token = "33333-33333-33333-3333"
    user.exponent_push_token = "3333-3333-333-33333"
    user.address = create_user_address_data()
    return user


def test_user_database():
    # data = create_user_data
    response = user_database.add_user(create_user_data())
    assert response is True
