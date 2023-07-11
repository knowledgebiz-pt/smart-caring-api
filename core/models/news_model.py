from mongoengine import Document, ObjectIdField, StringField, IntField, DictField, DateTimeField, BooleanField, EmbeddedDocument, EmbeddedDocumentField, ListField


class ModelContent(EmbeddedDocument):
    type = StringField()
    path = StringField()


class News(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    user_id = StringField()
    text = StringField()
    content = EmbeddedDocumentField(ModelContent)
    link = StringField()
    likes = ListField()
    favorites = ListField()
    date = StringField()

