from mongoengine import Document, ObjectIdField, StringField, DateField

class Schedule(Document):
    """
    Schedule model database
    """
    _id = ObjectIdField()
    id_user = StringField()
    event_title = StringField()
    event_description = StringField()
    date = DateField()