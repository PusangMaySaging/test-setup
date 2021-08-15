#mongo QuerySets 
# args:list of QuerySets
def querysets_to_dicts(query_sets):
    _list = []
    if(query_sets):
      for q in query_sets:
        temp = queryset_to_dict(q)
        _list.append(temp)
    return _list

#mongo QuerySet single
#args:QuerySet
def queryset_to_dict(query_set):
    temp = {}
    if(query_set):
        temp = query_set.to_mongo().to_dict()
        if '_id' in temp: 
            temp['_id'] = str(temp['_id'])
    return temp
 
