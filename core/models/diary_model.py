from mongoengine import Document, ObjectIdField, StringField, BooleanField

class Diary(Document):
    """
    Diary model database
    """
    _id = ObjectIdField()
    user_id = StringField()
    title = StringField()
    content = StringField()
    anexed_file = StringField()
    tags = StringField()
    public = BooleanField()
    