my_dict = {'tuple': (1, True, 'test', 15, 14.2), 'list': [12, 15, 33, 44, 7],
           'dict': {'Key_1': 10, 'Key_2': 11, 'Key_3': 45, 'Key_4': 99, 'Key_5': 0},
           'set': {1, 2, 'Alex', 'Anna', 'Maria'}}
tuple_value = my_dict['tuple']
print(tuple_value[-1])
list_value = my_dict['list']
list_value.append(13)
list_value.pop(1)
print(list_value)
dict_value = my_dict['dict']
dict_value['i am a tuple'] = True
dict_value.pop('Key_1')
print(dict_value)
set_value = my_dict['set']
set_value.add('hello')
set_value.remove(2)
print(set_value)
print(my_dict)
