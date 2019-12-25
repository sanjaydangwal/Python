from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wraper(*args,**kwargs):
        print(f"you call {any_function.__name__} function")
        print(any_function.__name__)
        return any_function(*args,**kwargs)
    return wraper

@decorator_function
def add(x,y):
    '''this function takes two parameaters and return its sum.'''
    return x+y

print(add(2,3))