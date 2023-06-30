from mongoengine import Document, ObjectIdField, StringField, DictField, DateTimeField, BooleanField, EmbeddedDocument, EmbeddedDocumentField, IntField


class ModelContent(EmbeddedDocument):
    type = StringField()
    path = StringField()


class ModelLink(EmbeddedDocument):
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
    link = DictField()
    likes = IntField()
    date = DateTimeField()

