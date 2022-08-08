import cards, games

class W_Card(cards.Card):
    J_VALUE = 11
    QUEEN_VALUE = 12
    KING_VALUE = 13
    ACE_VALUE = 14
    @property
    def value(self):
        if self.is_face_up:
            v = W_Card.RANKS.index(self.rank) + 1
        return v

class W_Deck(cards.Deck):
    ''' Колода игральных карт'''
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))

    def remains(self):
        return len(self.cards)


class W_Hand(cards.Hand):
    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + '\t' + super(W_Hand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep

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
            if card.value == W_Card.ACE_VALUE:
                contains_ace = True
                #card.value = W_Card.ACE_VALUE

        contains_j = False
        for card in self.cards:
            if card.value == W_Card.J_VALUE:
                contains_j = True
                #card.value = W_Card.J_VALUE

        contains_queen = False
        for card in self.cards:
            if card.value == W_Card.QUEEN_VALUE:
                contains_queen = True
                #card.value = W_Card.QUEEN_VALUE

        contains_king = False
        for card in self.cards:
            if card.value == W_Card.KING_VALUE:
                contains_king = True
                #card.value = W_Card.KING_VALUE


class W_Player(W_Hand):
    def lose(self):
        print(self.name, 'проиграл.')

    def win(self):
        print(self.name, 'победил.')

    def push(self):
        print(self.name, 'сыграл в ничью.')


class W_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)
        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def reload_deck(self):
        if self.deck.remains() < 30:
            self.deck.cards = []
            self.deck.populate()
            self.deck.shuffle()

    def play(self):
        self.deck.deal(self.players, per_hand=1)
        for player in self.players:
            print(player)

def main():
    print('\t\t Добро пожаловать за игровой стол блэк-джэка!\n')

    names = []
    number = games.ask_number('Сколько всего игроков? (1-7): ', low = 1, high= 8)
    for i in range(number):
        name = input('Введите имя игрока: ')
        names.append(name)
        print()

    game = W_Game(names)

    again = None
    while again != 'n':
        game.reload_deck()
        game.play()
        again = games.ask_yes_no('\nХотите сыграть еще раз? ')

main()

