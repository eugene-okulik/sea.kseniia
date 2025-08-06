def decision_maker(func):

    def wrapper(user_first_answer, user_second_answer):
        if user_first_answer == user_second_answer:
            return func(user_first_answer, user_second_answer, '+')
        elif (user_second_answer < 0) or (user_first_answer < 0):
            return func(user_first_answer, user_second_answer, '*')
        elif user_first_answer > user_second_answer:
            return func(user_second_answer, user_first_answer, '-')
        elif user_second_answer > user_first_answer:
            return func(user_first_answer, user_second_answer, '/')
    return wrapper


user_first_answer = int(input('What is your first digit?'))
user_second_answer = int(input('What is your second digit?'))


@decision_maker
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


result = calc(user_first_answer, user_second_answer)
print(result)
