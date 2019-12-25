
from functools import wraps
import time
def decorator(any_func):
    @wraps(any_func)
    def wraper(*args,**kwargs):
        t1 = time.time()
        any_func(*args,**kwargs)
        t2 = time.time()
        print(t2-t1)
    return wraper


@decorator
def func(n):
    print([i**2 for i in range(1,n+1)])

func(100)