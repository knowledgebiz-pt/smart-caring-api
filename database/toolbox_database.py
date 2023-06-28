from mongoengine import connect
import core.models as model
import json

import core.models.toolbox_model

#CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/smart-caring?retryWrites=true&w=majority'
CONNECTION = 'mongodb://localhost:27017/smartcaring?retryWrites=true&w=majority'

def add_toolbox(value):
    """
    Create new news article in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.toolbox_model.Toolbox(
        toolbox_name = value.tool_name,
        toolbox_description = value.tool_description,
        toolbox_image = value.tool_image,
        toolbox_languages = value.tool_languages,
        toolbox_rating = value.tool_rating,
        toolbox_website = value.tool_website,
        tool_tags = value.tool_tags,
        tool_category = value.tool_category,
        tool_price = value.tool_price
    ).save()
    return str(response.auto_id_0)


def return_toolbox_by_id(id_toolbox):
    connect(host=CONNECTION)
    response = model.toolbox_model.Toolbox.objects(_id = id_toolbox)
    response = json.loads(response.to_json()) if response is not None else None
    return response

def delete_toolbox_by_id(id_toolbox):
    connect(host=CONNECTION)
    response = model.toolbox_model.Toolbox.objects(_id = id_toolbox)
    response.delete()
    return response