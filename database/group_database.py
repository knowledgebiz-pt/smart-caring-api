from mongoengine import connect
import core.models as model
import json
import os
import core.models.group_model

CONNECTION = os.getenv('DATABASE_CONNECTION')


def add_group(value):
    """
    Create new group entry in database
    :param value:
    :return:
    """
    message = core.models.group_model.ModelMessage()
    message.type = value.type,
    message.content = value.content,
    message.date = value.date,
    message.id_user_sender = value.id_user_sender,
    message.deleted = value.deleted,
    message.sent = value.sent

    response = model.group_model.Group(
        user_id_creator = value.id_creator,
        users_ids_receivers = value.id_receiver,
        message = message
    ).save()
    return str(response.auto_id_0)


def return_group_by_id(id_group):

    response = model.group_model.objects(_id=id_group).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_group_by_user_id(id_user):
    response = model.group_model.objects(user_id = id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response