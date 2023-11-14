def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@memoize
def expensive_calculation(n):
    print(f"Calculating result for {n}:")
    return n * 2


print(expensive_calculation(3))
print(expensive_calculation(3))
print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(5))
