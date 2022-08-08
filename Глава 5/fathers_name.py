# Программа которая будет называть отца человека, по имени самого человека

glossary = {
    'Владислав Павлов' : "Виктор Павлов",
    'Виктор Павлов' : "Николай Павлов",
    "Полина Климова" : "Владимио Климов",
    "Евгений Ридченко" : "Виктор Ридченко"
}
choice = None
while choice != 0:
    print('''
    Список команда:
    0 - Выход
    1 - Посмотреть отца человека по его имени, фамили
    2 - Добавить пару "человек - отец"
    3 - Изменить пару "человек - отец"
    4 - Удалить пару "человек - отец"
    ''')
    choice = input('Введите ваш выбор: ')
    if choice == "0":
        print('До свидания')
    elif choice == "1":
        name = input("Введите имя, фамилию человека, отца которого вы хотите узнать: ")
        if name.title() in glossary:
            name = name.title()
            father = glossary[name]
            grandfather = glossary[father]
            print("Отец, человека под именем", name, "-", father, "а его дедушка - ", grandfather)
        else:
            print("Я не знаю этого человека")
    elif choice == "2":
        name = input("Кого вы желаете добавить в список?: ")
        if name.title() not in glossary:
            name = name.title()
            father = input('Введите имя, фамилию отца этого человека: ')
            glossary[name] = father
            print('Человек по имени', name, "добавлен в список.")
        else:
            print("Человек по имени", name, "уже есть в списке.")
    elif choice == "3":
        name = input("Введиете имя и фамилию человека, данные которого вы хотите поменять?: ")
        if name.title() in glossary:
            name = name.title()
            father = input("Введите имя и фамилию его отца: ")
            glossary[name] = father
            print('У человека по имени', name, "перепределен отец на", father)
        else:
            print("Указанного вами имени нет в списке.")
    elif choice == "4":
        name = ("Имя и фммилия человека, данные которого вы желаете удалить: ")
        if name.title() in glossary:
            name = name.title()
            del glossary[name]
            print('Данные о человеке по имени', name, "удалены из списка.")
        else:
            print("Такого человека нет в списке")