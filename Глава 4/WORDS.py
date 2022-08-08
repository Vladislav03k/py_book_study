# Игра "поле чудес": комьтер загадывает слово, игрок должен отгадать слово по буквам

import random

WORDS = ('слово', "попытка", "угадать", "сложно", "легко", "ответ", "подсказка")
word = random.choice(WORDS)
gamecount = 0
correct = word
len_word = len(word)
print('В слове', len_word, "букв.")
guess = None
new_word = ''
while (guess != correct and guess != '') and gamecount != 5:
    letter = input('Побробуйте отгадать букву: ')
    if letter.lower() in word:
        print('Да')
        new_word = new_word + ' ' + letter.lower()
        print('Буквы в слове: ', new_word)
        try_attempt = input('Попробуйте отгадать слово("да" или "нет")')
        if try_attempt == 'да':
            guess = input('Введите слово: ')
            if guess == correct:
                print('Поздравляем вы угадали слово с', gamecount, 'попытки.')
            elif guess != correct:
                print('Неверно, продолжайте отгадывать.')
                continue
        else:
            continue
    elif letter.lower() not in word:
        print('Нет')
        try_attempt = input('Попробуйте отгадать слово("да" или "нет")')
        gamecount += 1
        if try_attempt == 'да':
            guess = input('Введите слово: ')
            if guess == correct:
                print('Поздравляем вы угадали слово с', gamecount, 'попытки.')
            elif guess != correct:
                print('Неверно, продолжайте отгадывать.')
                continue
        else:
            continue
    break