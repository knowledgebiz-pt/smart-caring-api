from mongoengine import Document, ObjectIdField, StringField, DictField, DateTimeField

class News(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    user_id = StringField()
    title = StringField()
    content_type = StringField()
    content = DictField()
    date = DateTimeField()
