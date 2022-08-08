#Игра в аннограммы

import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble = ''
gamepoint = 0
gamecount = 1
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print('GAME')
print('Вот аннограмма: ', jumble)
guess = input('Попробуйте отгадать слово: ')
while guess != correct and guess != '':
    gamecount += 1
    answer = input('К сожалению, вы неправы. Нуждаетесть в подсказке(напиши "да" или "нет")')
    if answer == 'да':
        gamepoint -= 2
        print(correct[0:3])
        guess = input("Попробуйте отгадать исходное слово: ")
    elif answer == 'нет':
        guess = input("Попробуйте отгадать исходное слово: ")
    else:
        guess = input("Попробуйте отгадать исходное слово: ")
if gamecount == 1:

    gamepoint = 10
elif gamepoint >= 2 or gamepoint <=4:
    gamepoint += 8
else:
    gamepoint += 5
if guess == correct:
    print("Поздравляем, вы отгадали слово с", gamecount, "попытки и заработали", gamepoint, "очков.\n Спасибо за игру!")
