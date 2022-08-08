#Моя зверушка
#Виртуальный питомец о котором вы можете позаботиться
class Critter(object):
    ''' Виртуальный питомец'''
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = 'Объект класса Сritter\n'
        rep += 'меня зовут' + self.name + ', мне скучно на:' + str(self.boredom) + "очков, я хочу есть на" + str(self.hunger)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
            mood = 'прекрасно'
        elif unhapiness <= 10:
            mood = 'неплохо'
        elif unhapiness <= 15:
            mood = 'не сказать чтобы хорошо'
        else:
            mood = 'ужасно'
        return mood

    def talk(self):
        print('Меня зовут', self.name,', и сейчас я чувствую себя', self.mood,'\n')
        self.__pass_time()

    def eat(self, food = 1):
        count_f = 10
        while count_f >= 4:
            count_f = int(input('Введите количество еды: '))
            if count_f <= 4:
                print('Вы решили дать питомцу', count_f, 'порций еды.')
            else:
                print('Недостаточно еды')
        print('Мррр... Спасибо')
        food = count_f * food
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            print('Спасибо, я не голоден')
        self.__pass_time()

    def play(self, fun = 1):
        count_fun = 10
        while count_fun >= 4:
            count_fun = int(input('Ведите количество раз: '))
            if count_fun <= 4:
                print('Вы решили поиграть с питомцем', count_fun, 'раз')
            else:
                print('Не хватает энергии для игр')
        fun = count_fun * fun
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
            print('Спасибо, я наигрался')
        return self.__pass_time()

def main():
    crit_name = input('Как назовете свою зверюшку?: ')
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
        print(
            '''
            Моя зверюшка
            0 - выйти
            1 - Узнать самочувствие зверюшки
            2 - Покромить зверюшку
            3 - Поиграть со зверюшкой
            '''
        )
        choice = input("Ваш выбор: ")
        if choice == '0':
            print('До свидания')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        elif choice == 'info':
            print(crit)
        else:
            print('Неправильный ввод')

main()