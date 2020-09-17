def my_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return '1 \n 2 \n 3 \n'
    return wrapper
    time.sleep(1)
    @my_decorator
    def my_decorated_function(input):
        return input
    print(time.strftime("Today is %B %d, %Y.", time.localtime()))