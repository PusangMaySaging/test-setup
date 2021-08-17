from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from json import JSONEncoder
from bson import ObjectId

def create_hash(password):
    ph = PasswordHasher()
    hashed_password = ph.hajsh(password)
    return hashed_password

def verify_password(db_password, sent_password):
    try:
        ph = PasswordHasher()
        ph.verify(db_password, sent_password)
        return True
    except VerifyMismatchError:
        return False

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        # print(obj)
        # if isinstance(obj, dict):
        #     print("DICT")
        #     obj = self.convert_oid_dict_fields(obj)
        #     return obj

        if isinstance(obj, ObjectId):
            return str(obj)

        # if isinstance(obj, list):
        #     print("LIST")
        #     obj = self.serialize_list(obj)
        #     return obj
        # return super(CustomJSONEncoder,self).default(obj)
    

    # def convert_oid_dict_fields(self, _dict):
    #     new_dict = {}
    #     for key,value in _dict.items():
    #         if(isinstance(value, ObjectId)):
    #             new_dict[key] = str(value)
    #         else:
    #             new_dict[key] = value
    #     return new_dict

    # def serialize_list(self, _list):
    #     new_list = []
    #     for l in _list:
    #         if isinstance(l,dict):
    #             new_list.append(self.convert_oid_dict_fields(l))
    #         if isinstance(l, ObjectId) :
    #             new_list.append(str(l))
    #         new_list.append(l)
    #     return new_list