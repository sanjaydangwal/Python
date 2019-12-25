def func(input_list,**kwargs):
    if kwargs.get("reverse_str"):
        return [name[::-1].title() for name in input_list]
    else:
        return [name.title() for name in input_list]
    #return [name[::-1] for name in input_list]

string=['sanjay','vijay']
print(func(string))
print(func(string,reverse_str=True))