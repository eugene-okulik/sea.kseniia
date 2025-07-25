def guess_game(secret_number):
    while True:
        user_answer = int(input('Давай сыграем в игру - угадай число, которое я загадала '))
        if user_answer == secret_number:
            print('Поздравляю! Ты угадал, игра окончена')
            break
        else:
            print('Ты не угадал, попробуй еще раз')
            continue

guess_game(6)

