#Моя зверушка
#Виртуальный питомец о котором вы можете позаботиться
class Critter(object):
    ''' Виртуальный питомец'''
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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

    def eat(self, food = 4):
        print('Мррр... Спасибо')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            print('Спасибо, я не голоден')
        self.__pass_time()

    def play(self, fun = 4):
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
        else:
            print('Неправильный ввод')

main()