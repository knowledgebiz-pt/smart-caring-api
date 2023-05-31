from mongoengine import Document, ObjectIdField, StringField 

class News(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    title = StringField()
    content = StringField()
    user_id = StringField()
    picture = StringField()
    video = StringField()