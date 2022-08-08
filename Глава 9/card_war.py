import cards,games

class CW_Card(cards.Card):
    @property
    def value(self):
        if self.is_face_up:
            v = CW_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v

class CW_Deck(cards.Deck):
    ''' Колода игральных карт'''
    def populate(self):
        for suit in CW_Card.SUITS:
            for rank in CW_Card.RANKS:
                self.cards.append(CW_Card(rank, suit))

    def remains(self):
        return len(self.cards)


class CW_Hand(cards.Hand):
    ''' "Рука" - набор карт у одного игрока.'''
    def __init__(self, name):
        super(CW_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + '\t' + super(CW_Hand, self).__str__()
        #if self.total:
            #rep += '(' + str(self.total) + ')'
        return rep


class CW_Player(CW_Hand):
    '''Игрок в блэк-джэк'''

    def lose(self):
        print(self.name, 'проиграл.')

    def win(self):
        print(self.name, 'победил.')


class CW_Game(object):
    '''Игра в блэк-джэк'''
    def __init__(self, names):
        self.players = []
        for name in names:
            player = CW_Player(name)
            self.players.append(player)
        self.deck = CW_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def __additional_cards(self, player):
        while self.deck.remains() != 0:
            self.deck.deal([player])
            print(player)

    def play(self):
        self.deck.deal(self.players, per_hand= 26)
        #self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        #print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        #self.dealer.flip_first_card()
        #if not self.still_playing:
            #print(self.dealer)
        #else:
            #print(self.dealer)
            #self.__additional_cards(self.dealer)

            #if self.dealer.is_busted():
                #for player in self.still_playing:
                   #player.win()
            #else:
                #for player in self.still_playing:
                    #if player.total > self.dealer.total:
                        #player.win()
                    #elif player.total < self.dealer.total:
                        #player.lose()
                    #else:
                        #player.push()
        #for player in self.players:
            #player.clear()
        #self.dealer.clear(


