from mongoengine import DateTimeField, IntField, Document, ObjectIdField, StringField, BooleanField, EmbeddedDocumentField, EmbeddedDocument


class ModelUserAddress(EmbeddedDocument):
    street = StringField()
    city = StringField()
    country = StringField()
    postal_code = StringField()
    door_number = StringField()


class User(Document):
    """
    User model database
    """
    _id = ObjectIdField()
    name = StringField()
    email = StringField()
    user_gender = StringField()
    user_type = StringField()
    visibility = BooleanField()
    receives_notification = BooleanField()
    notification_email = StringField()
    password = StringField()
    picture = StringField()
    phone = StringField()
    birth_date = StringField()
    gmail_access_token = StringField()
    exponent_push_token = StringField()
    address = EmbeddedDocumentField(ModelUserAddress)


class ForgotPassword(Document):
    _id = ObjectIdField()
    user_email = StringField()
    code = IntField()
    created = StringField()


class UpdatePassword(Document):
    _id = ObjectIdField()
    email = StringField()
    new_password = StringField()


