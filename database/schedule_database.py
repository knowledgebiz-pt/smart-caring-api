from mongoengine import connect
import core.models as model
import json

import core.models.schedule_model

#CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'
CONNECTION = 'mongodb://localhost:27017/smartcaring?retryWrites=true&w=majority'
connect(host='mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority')

def add_schedule(value):
    """
    Create new Schedule event in database
    :param value:
    :return:
    """


    response = model.schedule_model.Schedule(
        event_title = value.event_title,
        event_description = value.event_description,
        date = value.date
    ).save()
    return str(response.auto_id_0)


def return_schedule_by_id(id_schedule):

    response = model.schedule_model.Schedule.objects(_id = id_schedule)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def return_schedule_by_user_id(id_user):

    response = model.schedule_model.Schedule.objects(user_id = id_user)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def delete_schedule_by_id(id_schedule):

    response = model.schedule_model.Schedule.objects(_id = id_schedule)
    response.delete()
    return response