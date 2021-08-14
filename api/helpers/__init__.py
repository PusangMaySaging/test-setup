
def serialize_dict_list(objectList): #list of dict
    arr=[]
    for l in objectList():
        if '_id' in l:
            l['_id'] = convert_to_string(l['_id'])
        arr.append(l)
    return arr

def convert_to_string(field):
    return str(field)
