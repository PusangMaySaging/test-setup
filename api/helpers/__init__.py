import jsonpickle
import json
def serialize_dict_list(objectList): #list of dict
    arr=[]
    for l in objectList:
        # if '_id' in l:
        #     l['_id'] = convert_to_string(l['_id'])
        print(l)
        arr.append(l)
        
    return arr

def convert_to_string(field):
    return str(field)

def to_list_of_dict(qList): #takes list of QuerySet
    result = [entry for entry in qList] 
    return result
