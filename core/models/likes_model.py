from mongoengine import Document, ObjectIdField, StringField, BooleanField

class Likes(Document):
    """
    Likes model database
    """
    _id = ObjectIdField()
    is_like = BooleanField()
    user_id = StringField()
    news_id = StringField()