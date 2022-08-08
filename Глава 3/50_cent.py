# Программа "монетка" которая подбрасывает монетку 100 раз и определяет количество выпадения орла и решки

import random


count = 0
heads_cnt = 0
tales_cnt = 0
while count != 100:
    cent = random.randrange(2) + 1
    count +=1
    if cent == 1:
        heads_cnt += 1
    elif cent == 2:
        tales_cnt += 1
print(f'Орел выпал ', heads_cnt, ' раз\n', 'Решка выпала ', tales_cnt, ' раз')