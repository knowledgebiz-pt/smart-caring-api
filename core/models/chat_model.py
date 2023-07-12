from mongoengine import Document, ObjectIdField, StringField, BooleanField, DateTimeField, EmbeddedDocumentField, EmbeddedDocument


class ModelMessage(EmbeddedDocument):
    type = StringField()
    content = StringField()
    date = DateTimeField()
    id_user_sender = StringField()
    id_user_receiver = StringField()
    deleted = BooleanField()
    viewed = BooleanField()
    sent = BooleanField()


class Chat(Document):
    """
    Chat model database
    """   
    _id = ObjectIdField()
    user_id_sender = StringField()
    user_id_receiver = StringField()
    message = EmbeddedDocumentField(ModelMessage)