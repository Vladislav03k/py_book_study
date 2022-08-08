#Генератор персонажей для ролевой игры

power = 0
health = 0
wisdom = 0
ability = 0
points = 30
print('Всего доступнно очков', points)
choice_1 = None
while choice_1 != '0':
    print("Давайте присвоим персонажам характеристики\n\n")
    print('''
    0 - Выход
    1 - Присвоить персонажу очки навыка
    2 - Откатить очки навыка у персонажа
    ''')
    choice_1 = input("\n\n\tВедите цифру: ")
    if choice_1 == '0':
        print('До свидания, хозяин!')
    elif choice_1 == '1':
        while points != 0 and choice_1_01 == '0':
        print('Выберите характеристику персонажа, которую желаете изменить.')
        print('''
        0 - Выход
        1 - Сила
        2 - Здоровье
        3 - Мудрость
        4 - Ловкость
        ''')
        choice_1_01 = input("\n\n\tВедите цифру: ")
        if choice_1_01 == '1':
            point_count = int(input('Введите количество очков, которое вы желаете добавить: '))
            if point_count <= points:
                power += point_count
                points -= point_count

                print('Количество очков силы:', power)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков силы:', power)
                print('Количество доступный очков:', points)
                continue
        elif choice_1_01 == '2':
            point_count = int(input('Введите количество очков, которое вы желаете добавить: '))
            if point_count <= points:
                health += point_count
                points -= point_count
                print('Количество очков здоровья:', health)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков здоровья:', health)
                print('Количество доступный очков:', points)
                continue
        elif choice_1_01 == '3':
            point_count = int(input('Введите количество очков, которое вы желаете добавить: '))
            if point_count <= points:
                wisdom += point_count
                points -= point_count
                print('Количество очков мудрости:', wisdom)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков мудрости:', wisdom)
                print('Количество доступный очков:', points)
                continue
        elif choice_1_01 == '4':
            point_count = int(input('Введите количество очков, которое вы желаете добавить: '))
            if point_count <= points:
                ability += point_count
                points -= point_count
                print('Количество очков ловкости:', ability)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков ловкости:', ability)
                print('Количество доступный очков:', points)
                continue
        else:
            print('Неправильный ввод данных!')
            if_exit = input('Желаете покинуть программу?("да" или "нет"')
            if if_exit == "нет":
                continue
            else:
                print('До свидания')
                break
    elif choice_1 == '2':
        print('Выберите характеристику персонажа, которую желаете изменить.')
        print('''
        0 - Выход
        1 - Сила
        2 - Здоровье
        3 - Мудрость
        4 - Ловкость
        ''')
        choice_1_01 = input("\n\n\tВедите цифру: ")
        if choice_1_01 == '1':
            point_count = int(input('Введите количество очков, которое вы желаете отбавить: '))
            if power >= 0 and power <= point_count:
                power -= point_count
                points += point_count
                print('Количество очков силы:', power)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков силы:', power)
                print('Количество доступный очков:', points)
                continue
        elif choice_1_01 == '2':
            point_count = int(input('Введите количество очков, которое вы желаете отбавить: '))
            if health >= 0 and health <= point_count:
                health -= point_count
                points += point_count
                print('Количество очков здоровья:', health)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков здоровья:', health )
                print('Количество доступный очков:', points)
                continue
        elif choice_1_01 == '3':
            point_count = int(input('Введите количество очков, которое вы желаете отбавить: '))
            if wisdom >= 0 and wisdom <= point_count:
                wisdom -= point_count
                points += point_count
                print('Количество очков мудрости:', wisdom)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков мудрости:', wisdom)
                print('Количество доступный очков:', points)
                continue
        elif choice_1_01 == '4':
            point_count = int(input('Введите количество очков, которое вы желаете отбавить: '))
            if ability >= 0 and ability <= point_count:
                ability -= point_count
                points += point_count
                print('Количество очков ловкости:', ability)
                print('Количество доступный очков:', points)
            else:
                print("Не хватает очков!")
                print('Количество очков ловкости:', ability)
                print('Количество доступный очков:', points)
                continue
        else:
            print('Неправильный ввод данных!')
            if_exit = input('Желаете покинуть программу?("да" или "нет"')
            if if_exit == "нет":
                continue
            else:
                print('До свидания')
                break
print('Количество очков силы:', power)
print('Количество очков здоровья:', health)
print('Количество очков мудрости:', wisdom)
print('Количество очков ловкости:', ability)
print('Количество доступный очков:', points)

