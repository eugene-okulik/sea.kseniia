import random


def reply_analizer():
    while True:
        salary = input('What is your salary? Your answer should look like $xxxxx ')
        if salary.startswith('$'):
            salary = salary[1:]
            if len(salary) == 0:
                print("Looks like you didn't enter digits")
                continue
            flag = True
            for char in salary:
                if not char.isdigit():
                    print("Your answer can't consist anything besides $ symbol and digits")
                    flag = False
                    break
            if not flag:
                continue
            else:
                return int(salary.strip('$'))
        else:
            print('Please start your answer with $ symbol')
            continue


salary = reply_analizer()
bonus = [True, False]
bonus_randomizer = random.choice(bonus)
if bonus_randomizer:
    spare_money = random.randrange(300, 1000)
    final_money = salary + spare_money
else:
    final_money = salary


print(f'{salary},{bonus_randomizer} - ${final_money}')
