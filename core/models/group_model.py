from mongoengine import ListField ,Document, ObjectIdField, StringField, BooleanField, DateTimeField, EmbeddedDocumentField, EmbeddedDocument

class ModelMessage(EmbeddedDocument):
    type = StringField()
    content = StringField()
    date = DateTimeField()
    id_user_sender = StringField()
    deleted = BooleanField()
    sent = BooleanField()

class Group(Document):
    """
    Group model database
    """   
    _id = ObjectIdField()
    user_id_creator = StringField()
    users_ids_receivers = ListField()
    message = EmbeddedDocumentField(ModelMessage)