a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'


def index(sring):
    universal_index = sring.index(':')
    return universal_index


a_index = index(a)
b_index = index(b)
c_index = index(c)


def slicing(string, index):
    sliced_string = string[index + 1:]
    return sliced_string.strip()


sliced_string_a = int(slicing(a, a_index))
sliced_string_b = int(slicing(b, b_index))
sliced_string_c = int(slicing(c, c_index))

a_adding = sliced_string_a + 10
b_adding = sliced_string_b + 10
c_adding = sliced_string_c + 10
print(a_adding, b_adding, c_adding)
