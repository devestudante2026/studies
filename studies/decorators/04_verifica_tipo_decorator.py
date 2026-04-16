def check_type(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                print("Some argument isn't of the 'int' type...")
                return None
        print("Everything is fine...")
    return wrapper

@check_type
def my_numbers(numbers):
    return numbers

my_numbers(3, 1, "4")#