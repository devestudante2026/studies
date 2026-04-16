def double_value(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double_value
def my_number(n):
    return n

#print(my_number(39))