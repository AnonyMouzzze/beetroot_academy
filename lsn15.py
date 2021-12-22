from functools import wraps

# Task 1
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called with {args} {kwargs}')

    return wrapper

@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Task 2
def stop_words(words: list):
    def wrapper(func):
        @wraps(func)
        def replace_words(*args, **kwargs):
            slogan = func(*args, **kwargs)
            for word in words:
                if word in slogan:
                    slogan = slogan.replace(word, '*')
            return slogan
        return replace_words
    return wrapper

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))

# Task 3
def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        @wraps(func)
        def rules(*args, **kwargs):
            string = func(*args, **kwargs)
            print(string)
            if len(string) <= max_length and type(string) == type_:
                for word in contains:
                    if word not in string:
                        return False
                return string
            return False
        return rules
    return wrapper


@arg_rules(type_=str, max_length=50, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'