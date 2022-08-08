import random

def ask_yes_no(question):
    """ Задают вопрос с ответом 'yes' или 'no'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(low = 0, high = 100, multiple = 1):
    response = None
    while response not in range(low,high,multiple):
        response = int(input('Введите число'))
        question = ask_yes_no('Желаете ли вы ввести кратность чисел?(у/n)')
        if question == 'y':
            multiple = int(input('Введите шаг(кратность): '))
        else:
            continue
    return response

def main():
    the_number = random.randint(1,100)
    guess = ask_number()
    tries = 1
    while guess != the_number and tries != 10:
        if guess > the_number:
            print('Меньше...')
        elif guess == the_number:
            print("Поздравляем вы угадали число: ", the_number)
        else:
            print('Больше...')
        guess = ask_number()
        tries += 1
        if tries == 10:
            print('Попытки закончились...')
            break
        else:
            continue

main()
