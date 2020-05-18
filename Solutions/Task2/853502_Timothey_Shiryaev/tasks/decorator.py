from functools import wraps
def memory(fun):

    @wraps(fun)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(sorted(kwargs.items())))
        try:
            return cache[key]
        except KeyError:
            ret = cache[key] = fun(*args, **kwargs)
        return ret
    cache = {}
    return wrapper

@memory
def fibonacci(n):
    if n < 2 :
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

#print(fibonacci(5))
#print(fibonacci(4))

