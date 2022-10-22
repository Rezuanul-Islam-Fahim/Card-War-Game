from random import shuffle


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8,  'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.card_list = []

        for suit in suits:
            for rank in ranks:
                self.card_list.append(Card(suit, rank))

    def shuffle_list(self):
        shuffle(self.card_list)

    def deal_one(self):
        return self.card_list.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def remove_one(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


player_one = Player('Fahim')
player_two = Player('Karim')
deck = Deck()
deck.shuffle_list()

for x in range(int(len(deck.card_list)/2)):
    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())
