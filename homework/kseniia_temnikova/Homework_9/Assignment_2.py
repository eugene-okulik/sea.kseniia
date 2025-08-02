temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
                27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

# def is_hot(x):             - еще один вариант решения
#     return x > 28

# new_temperatures = filter(is_hot,temperatures)
# print(list(new_temperatures))

new_temperatures = filter(lambda x: x >28, temperatures)
print(list(new_temperatures))
print(max(temperatures))
print(min(temperatures))
average = sum(temperatures) / len(temperatures)
print(round(average))
