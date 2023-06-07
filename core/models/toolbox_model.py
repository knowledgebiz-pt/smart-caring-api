from mongoengine import Document, ObjectIdField, StringField 

class Toolbox(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    toolname = StringField()
    tooldescription = StringField()
    toolimage = StringField()
    toollanguages = StringField()
    