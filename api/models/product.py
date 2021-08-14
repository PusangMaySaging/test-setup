from mongoengine import Document,StringField

class Product(Document):
    name = StringField(max_length=200, required=True)