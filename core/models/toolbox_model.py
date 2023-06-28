from mongoengine import Document, ObjectIdField, StringField 

class Toolbox(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    tool_name = StringField()
    tool_description = StringField()
    tool_image = StringField()
    tool_languages = StringField()
    tool_rating = StringField()
    tool_website = StringField()
    tool_tags = StringField()
    