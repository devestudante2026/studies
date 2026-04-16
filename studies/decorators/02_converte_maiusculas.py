def upper_converter(func):
    def wrapper(*args, **kwargs):
        formatted = func(*args, **kwargs).upper()
        return formatted
    return wrapper

@upper_converter
def my_msg(msg):
    return msg

#my_msg("it's all small here...")
