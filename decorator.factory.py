#!/usr/bin/python

from functools import wraps

def max_value(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*arg,**kwarg):
            result=func(*arg,**kwarg)
            if result > threshold:
               print('Result is too big ({0}).Max allowed is ({1}).'.format(result,threshold))
            return result
        return wrapper

    return decorator


@max_value(75)
def cube(n):
    return n**3


print(cube(5))
            
