from functools import wraps
def decorator(only_data):
    def only_int(func):
        @wraps(func)
        def wraper(*args,**kwargs):
            if(all((type(i)==only_data for i in args))):
                return func(*args,**kwargs)
            return "invalid input"
        return wraper
    return only_int


@decorator(str)
def  add(*args,**kwargs):
    '''this is add function'''
    total = None
    for i in args:
        total+=i
    return total


print(add('sanjay',' dangwal'))