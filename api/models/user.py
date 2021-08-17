from mongoengine import Document,StringField, IntField, EmailField, EnumField
from helpers.database import querysets_to_dicts,queryset_to_dict
from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    USER = "user"

class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    mobile_number = StringField(required=True, unique=True)
    role = EnumField(Role,default=Role.USER)
    meta = {'collection':'users'}

    def createOne(self, data):
        self.name = data.get('name', None)
        self.email = data.get('email', None)
        self.password = data.get('password', None)
        self.mobile_number = data.get('mobile_number', None)
        self.role = data.get('role', None)
        self.save()

    @classmethod
    def get(cls, filters={}, projections=None):
        #list of producs
        if(projections):
           return querysets_to_dicts(cls.objects(__raw__ = filters).only(*projections))
        return querysets_to_dicts(cls.objects(__raw__ = filters))

    @classmethod
    def getOne(cls, filters={}, projections=None):
       if(projections):
           print("HAS PROJECTION")
           print(projections)
           return queryset_to_dict(cls.objects(__raw__ = filters).only(*projections).first())
       return queryset_to_dict(cls.objects(__raw__ = filters).first())