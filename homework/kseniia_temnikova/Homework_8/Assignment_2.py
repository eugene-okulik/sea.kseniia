import sys

sys.set_int_max_str_digits(25000)


def fibonachi():
    num_previous = 0
    num_new = 1
    num_buffer = 0
    count = 1
    while True:
        if count == 1:
            count += 1
            yield 0
            continue
        if count == 2:
            count += 1
            yield 1
            continue
        num_buffer = num_new
        num_new = num_new + num_previous
        num_previous = num_buffer
        count += 1
        yield num_new


count = 0
for number in fibonachi():
    count += 1
    if count == 20:
        print(f'count ={count}, number={number}')
        continue
    if count == 200:
        print(f'count ={count}, number={number}')
        continue
    if count == 1000:
        print(f'count ={count}, number={number}')
        continue
    if count == 100000:
        print(f'count ={count}, number={number}')
        break
