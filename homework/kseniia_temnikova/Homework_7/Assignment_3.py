a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'


def index(string):
    universal_index = string.index(':')
    return universal_index


def slicing(string):
    sliced_string = string[index(string) + 1:]
    return sliced_string.strip()


def adding(string):
    final_number = int(slicing(string)) + 10
    return final_number


print(adding(a), adding(b), adding(c), adding(d))
