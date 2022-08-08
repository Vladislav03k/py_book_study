class TV(object):
    def __init__(self, user, volume = 0, chanel = 0):
        self.user = user
        self.volume = volume
        self.chanel = chanel

    def choose_chanel(self):
        new_chanel = 0
        while new_chanel <= 0 or new_chanel > 100:
            new_chanel =int(input('Введите номер канала: '))
            if new_chanel <= 0:
                print('Номер канала не может быть отрицательным и нулевым')
            else:
                print("Достпуно только 100 каналов")
        self.chanel = new_chanel

    def minus_volume(self):
        self.volume -= 1
        if self.volume <= 0:
            self.volume = 0
            print('Достигнут минимальный предел звука')

    def plus_volume(self):
        self.volume += 1
        if self.volume >= 100:
            self.volume = 100
            print('Достигнут максимальный предел звука')

    def info(self):
        print('Channel:', self.chanel)
        print('Volume:', self.volume)

def main():
    user_name = input('Введите имя пользователя:')
    user = TV(user_name)
    choice = None
    while choice != '0':
        print('''
        Меню телевизора:
        0 - Выключить
        1 - Выбрать канал
        2 - Убавить звук
        3 - Добавить звук
        ''')
        choice = input('Ваш выбор: ')
        if choice == '0':
            print('Выключась')
        elif choice == '1':
            user.choose_chanel()
            user.info()
        elif choice == '2':
            user.minus_volume()
            user.info()
        elif choice == '3':
            user.plus_volume()
            user.info()
        else:
            print('Данная функция отсутсвует')

main()