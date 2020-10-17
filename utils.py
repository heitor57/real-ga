def dict_to_list_gen(d):
    for k, v in zip(d.keys(), d.values()):
        if v == None:
            continue
        yield k
        yield v

def dict_to_list(d):
    return list(dict_to_list_gen(d))

def get_parameters_name(parameters):
    # parameters = {k:v for k,v in parameters if v}
    list_parameters=list(map(str,dict_to_list(parameters)))
    return '_'.join(list_parameters)
