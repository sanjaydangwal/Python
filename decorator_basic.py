from functools import wraps
def decorator_fun(any_func):
    @wraps(any_func)
    def new_func(*agrs,**kwargs):
        print("we have inhenced function")
        return any_func(*agrs,**kwargs)
    return new_func
@decorator_fun
def func1(x,y):
    return x+y
@decorator_fun
def func2(x):
    '''hello it is halala'''
    print(f"it is function 2 with {x}")
print(func1(4,2))
func2(20)

print(func2.__doc__)