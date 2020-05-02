def memory(func):
    cache = {}
    def decorate(*arg):
        result = cache.get(arg)
        if result is None:
            result = cache[arg] = func(*arg)
        # print('Already in cache')
        return result

    return decorate

@memory
def fibonacci(n):
    if n < 2 :
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(5))
print(fibonacci(4))

