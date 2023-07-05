from mongoengine import Document, ObjectIdField, StringField, DictField, DateTimeField, BooleanField, EmbeddedDocument, EmbeddedDocumentField, ListField


class ModelContent(EmbeddedDocument):
    type = StringField()
    path = StringField()


class Comment(Document):
    """
    Comment model database
    """
    _id = ObjectIdField()
    news_id = StringField()
    comment_reply_id = StringField()
    user_id = StringField()
    text = StringField()
    link = StringField()
    likes = ListField()
    date = StringField()

