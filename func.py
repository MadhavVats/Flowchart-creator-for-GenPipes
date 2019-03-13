import sys
from functools import wraps

class TraceCalls(object):
    """ Use as a decorator on functions that should be traced. Several
        functions can be decorated - they will all be indented according
        to their call depth.
    """
        
    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            #To check if a function is called inside a function
            ret = fn(*args, **kwargs)
            global functions_called
            functions_called.append(fn.__name__)
            return ret
        return wrapper


functions_called = []
def fun_called():
    return(functions_called)

