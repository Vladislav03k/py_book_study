#список слов в случайном порядке

import random

WORDS = ['слово', "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
count = 0
word = ""
random_words = []
while count != len(WORDS):
    word = random.choice(WORDS)
    count += 1
    #if word not in random_words:
    random_words.append(word)
    #elif word in random_words:
        #continue
    #break
print(random_words)


