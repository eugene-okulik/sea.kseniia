fuzz_buzz_range = list(range(1, 101))
print(fuzz_buzz_range)
for digit in fuzz_buzz_range:
    if (digit % 3 == 0) and (digit % 5 == 0):
        print('FuzzBuzz')
    elif digit % 5 == 0:
        print('Buzz')
    elif digit % 3 == 0:
        print('Fuzz')
    else:
        print(digit)
