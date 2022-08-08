#Блэк-джэк
#От 1 до 7 игроков против диллера
import cards, games

class BJ_Card(cards.Card):
    '''Карты для игры в Блэк-джэк'''
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    ''' Колода игральных карт'''
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

    def remains(self):
        return len(self.cards)

class BJ_Hand(cards.Hand):
    ''' "Рука" - набор карт у одного игрока.'''
    def __init__(self, name, credit = 500):
        super(BJ_Hand, self).__init__()
        self.name = name
        self.credit = credit

    def __str__(self):
        rep = self.name + '\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        if self.credit:
            rep += '\t' + 'credits: ' + str(self.credit)
        return rep

    def stavka(self, stavka):
        ''' вычитает из кредита игрока размер ставки'''
        self.credit -= stavka


    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    '''Игрок в блэк-джэк'''
    def is_hitting(self):
        response = games.ask_yes_no('\n' + self.name + ' будуте брать еще карты?(y/n): ')
        return response == 'y'

    def bust(self):
        print(self.name, 'перебрал.')
        self.lose()

    def lose(self):
        print(self.name, 'проиграл.')

    def win(self):
        print(self.name, 'победил.')

    def push(self):
        print(self.name, 'сыграл с компьютером в ничью.')


class BJ_Dealer(BJ_Hand):
    '''Диллер в игре блэк-джэк'''
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, 'перебрал.')

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    '''Игра в блэк-джэк'''
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer('Dealer')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.kon = 0
        self.stavka = 100

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp


    def reload_deck(self):
        if self.deck.remains() < 30:
            self.deck.cards = []
            self.deck.populate()
            self.deck.shuffle()

    def is_bankrot(self):
        for player in self.players:
            if player.credit <= 0:
                print(f'Игрок {player.name} покинул игру, так как стал банкротом.')
                self.players.remove(player)

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.is_bankrot()
        for player in self.players:
            player.stavka(self.stavka)
            self.kon += self.stavka
        self.dealer.stavka(self.stavka)
        self.kon += self.stavka
        print(f'На кону {self.kon} кредитов\n')
        self.deck.deal(self.players + [self.dealer], per_hand= 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
            self.dealer.credit += self.kon
            self.kon = 0
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
                    player.credit += self.kon/len(self.still_playing)
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                        player.credit += self.kon
                        self.kon = 0
                    elif player.total < self.dealer.total:
                        player.lose()
                        self.dealer.credit += self.kon
                        self.kon = 0
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()
        self.kon = 0


def main():
    print('\t\t Добро пожаловать за игровой стол блэк-джэка!\n')

    names = []
    number = games.ask_number('Сколько всего игроков? (1-7): ', low = 1, high= 8)
    for i in range(number):
        name = input('Введите имя игрока: ')
        names.append(name)
        print()

    game = BJ_Game(names)

    again = None
    while again != 'n' and len(game.still_playing) != 0:
        game.reload_deck()
        game.play()
        again = games.ask_yes_no('\nХотите сыграть еще раз? ')

main()

input('\n\n Нажмите Enter, чтобы выйти. ')