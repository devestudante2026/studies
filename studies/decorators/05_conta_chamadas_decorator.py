def counts_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        print(f"Function '{func.__name__}' already run {count} times.")
        return result
    return wrapper

@counts_calls
def decorated_sum(x, y):
    return x+y

#print(decorated_sum(3, 4))
#print(decorated_sum(10, 5))