# первый вариант решения
# def repeat_me(func):
#
#     def wrapper(text, count):
#         while count > 0:
#             func(text)
#             count -= 1
#     return wrapper
#
#
# @repeat_me
# def example(text):
#     print(text)
#
#
# example('print me', count=2)

# второй вариант решения
def repeat_me(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_count = count
            while new_count > 0:
                func(*args, **kwargs)
                new_count -= 1
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
