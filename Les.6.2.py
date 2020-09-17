def my_decorator(input_arg):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f'{input_arg}\n{result}\n{input_arg}'

        return wrapper

    return the_real_decorator
import time
@my_decorator('-------------')
def my_decorated_function(input):
    return input


print(time.strftime("Today is %B %d, %Y.", time.localtime()))
