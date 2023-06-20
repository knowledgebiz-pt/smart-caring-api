from mongoengine import Document, ObjectIdField, StringField, DictField, DateTimeField, BooleanField, EmbeddedDocument, EmbeddedDocumentField


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
    title = StringField()
    content = EmbeddedDocumentField(ModelContent)
    link = EmbeddedDocumentField(ModelLink)
    date = DateTimeField()

