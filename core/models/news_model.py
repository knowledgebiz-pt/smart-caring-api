from mongoengine import Document, ObjectIdField, StringField, DictField, DateTimeField, BooleanField, EmbeddedDocument, EmbeddedDocumentField, IntField


class ModelContent(Document):
    type = StringField()
    path = StringField()


class ModelLink(Document):
    path = StringField()
    show_preview = BooleanField()


class News(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    user_id = StringField()
    text = StringField()
    content = EmbeddedDocumentField(ModelContent)
    link = EmbeddedDocumentField(ModelLink)
    likes = IntField()
    date = DateTimeField()

