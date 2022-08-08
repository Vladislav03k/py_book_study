import random

#from debugpy._vendored.pydevd.pydev_sitecustomize.sitecustomize import raw_input


def build_deck():
    ranks = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = ['D', 'H', 'S', 'C']
    deck = [rank + suit
            for rank in ranks for suit in suits]
    random.shuffle(deck)

    return deck

def card_value():
    face_cards = ['J', 'Q', 'K', 'A']

    if card[0] in face_cards:
        return face_cards.index(card[0]) + 11
    else:
        return int(card[0])


def clean_up(pile_one, pile_two):
    if not pile_one[-1]:
        pile_one.pop()
    if not pile_two[-1]:
        pile_two.pop()

def card_choice(pile):
    if pile[-1]:
        return random.choice(pile[-3:])
    else:
        return pile[-2]

def replace_cards(deck, pile_one, pile_two):
    pile_one.extend(pile_two)
    random.shuffle(pile_one)
    deck.extend(pile_one)

def play_war():
    deck = build_deck()
    battle_stat, war_stat, double_war_stat = 0, 0, 0
    pile_one, pile_two, deck_one, deck_two = [], [], [], []

    for i in xrange(26):
        deck_one.append(deck.pop())
        deck_two.append(deck_two.pop())

    while deck_one and deck_two:
        del pile_one[:], pile_two[:]
        pile_one.append(deck_one.pop())
        pile_two.append(deck_two.pop())

        if card_value(pile_one[0]) > card_value(pile_two[0]):
            battle_stat += 1
            replace_cards(deck_one, pile_one, pile_two)

        elif card_value(pile_one[0]) < card_value(pile_two[0]):
            battle_stat += 1
            replace_cards(deck_two, pile_one, pile_two)

        else:

            war_count = 1

            while True:
                battle_stat += 1
                war_stat += 1

                for i in xrange(3):
                    if deck_one:
                        pile_one.append(deck_one.pop(0))
                    elif pile_one[-1]:
                        pile_one.append('')

                if card_value(card_choice(pile_one)) > card_value(card_choice(pile_two)):
                    clean_up(pile_one, pile_two)
                    replace_cards(deck_one, pile_one, pile_two)
                    if war_count == 2:
                        double_war_stat += 1
                    break

                elif card_value(card_choice(pile_one)) < card_value(card_choice(pile_two)):
                    clean_up(pile_one, pile_two)
                    replace_cards(deck_two, pile_one, pile_two)
                    if war_count == 2:
                        double_war_stat += 1
                    break

                war_count += 1
    return battle_stat, war_stat, double_war_stat

def war_stats(n):
    battle_stat, war_stat, double_war_stat = 0.0, 0.0, 0.0

    for i in range(n):
        result = play_war()
        battle_stat += result[0]
        war_stat += result[1]
        double_war_stat += result[2]

    print('Avg of battles' + str(battle_stat))
    print('Avg of wars' + str(war_stat))
    print('Avg of double wars' + str(double_war_stat))


while True:
    selection = int(input('How mane games of war would you like to play? ("q" to exit): '))

    try:
        if selection.lower()[0] == 'q':
            break

        elif 0 < int(selection):
            war_stats(int(selection))

        else:
            print('Please enter an integer between 1 and 1000')

    except:
        print('Please enter an integer between 1 and 1000')

