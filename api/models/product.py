from mongoengine import Document,StringField, IntField
from helpers.database import querysets_to_dicts,queryset_to_dict
class Product(Document):
    name = StringField(max_length=200, required=True)
    price = IntField(min=0, required=True)
    meta = {'collection': 'products'}
    
   
    def createOne(self, data):
       self.name = data.get('name', None)
       self.price = data.get('price', None)
       self.save()

    def createMany(self, data_list):
       for data in data_list:
          Product(**data).save()

    @classmethod
    def get(cls,filters={}, projections=None):
        #list of producs
        if(projections):
           return list(cls.objects(__raw__ = filters).as_pymongo().only(*projections))
        return list(cls.objects(__raw__ = filters).as_pymongo())
    
    @classmethod
    def getOne(cls, filters={}, projections=None):
        #single product
        if(projections):
           return cls.objects(__raw__ = filters).as_pymongo().only(*projections).first()
        return cls.objects(__raw__ = filters).as_pymongo().first()
    

