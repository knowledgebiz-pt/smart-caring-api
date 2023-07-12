from mongoengine import connect
import core.models as model
import json
import core.models.chat_model
import os

connect(host=os.getenv('DATABASE_CONNECTION'))


def add_chat(value):
    """
    Create new chat entry in database
    :param value:
    :return:
    """

    # message = core.models.chat_model.ModelMessage()
    # message.type = value.type,
    # message.content = value.content,
    # message.date = value.date,
    # message.id_user_sender = value.id_user_sender,
    # message.id_user_receiver = value.id_user_receiver,
    # message.deleted = value.deleted,
    # message.viewed = value.viewed,
    # message.sent = value.sent
    print("here")
    print(value)
    print(value["user_id_sender"])

    response = model.chat_model.Chat(
        user_id_sender=value["user_id_sender"],
        user_id_receiver=value["user_id_receiver"],
        message={
            "type": "msg",
            "content": value["message"],
            "date": value["date"],
            "id_user_sender": value["user_id_sender"],
            "id_user_receiver": value["user_id_receiver"],
            "deleted": value["deleted"],
            "viewed": value["viewed"],
            "sent": value["sent"]
        }
    ).save()
    return str(response.auto_id_0)


def return_chat_by_id(id_chat):
    response = model.chat_model.Chat.objects(_id=id_chat).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response


def return_chat_by_user_id(id_user):
    response = model.chat_model.Chat.objects(user_id=id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response
