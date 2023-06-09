from mongoengine import connect
import core.models as model
import json
import os


connect(host=os.getenv('DATABASE_CONNECTION'))


def add_diary(value):
    """
    Create new diary entry in database
    :param value:
    :return:
    """


    response = model.diary_model.Diary(
        user_id = value.user_id,
        title = value.title,
        content = value.content,
        anexed_file = value.anexed_file,
        tags = value.tags,
        public = value.public,
    ).save()
    return str(response.auto_id_0)


def return_diary_by_id(id_diary):

    response = model.diary_model.Diary.objects(_id = id_diary)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_diary_by_user_id(id_user):

    response = model.diary_model.Diary.objects(user_id = id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def delete_diary_by_id(id_diary):

    response = model.diary_model.Diary.objects(_id = id_diary)
    response.delete()
    return response