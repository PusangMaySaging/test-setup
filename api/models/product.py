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
    def get(cls, projections=None, filters={}):
        #list of producs
        if(projections):
           return querysets_to_dicts(cls.objects(__raw__ = filters).only(*projections))
        return querysets_to_dicts(cls.objects(__raw__ = filters))
    
    @classmethod
    def getOne(cls, projections=None, filters={}):
        #single product
        if(projections):
           return queryset_to_dict(cls.objects(__raw__ = filters).only(*projections)).first()
        return queryset_to_dict(cls.objects(__raw__ = filters)).first()
    

