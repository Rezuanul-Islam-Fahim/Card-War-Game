from random import shuffle


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8,  'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# ========== Card class ===========
# =================================
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# ========== Deck class ===========
# =================================
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


# =========== Player class ===============
# ========================================
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


# ========== Main game function ============
# ==========================================
def run_game():

    player_one = Player('Fahim')
    player_two = Player('Karim')
    deck = Deck()
    deck.shuffle_list()
    rounds = 1
    game_on = True

    for x in range(int(len(deck.card_list)/2)):
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())

    while game_on:
        print(f'Round {rounds}')

        if len(player_one.all_cards) == 0:
            print('Player two wins')
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print('Player one wins')
            game_on = False
            break

        war_on = True
        player_one_cards = []
        player_two_cards = []
        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

        while war_on:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                war_on = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                war_on = False
            else:
                print('WAR!!!!!')

                if (len(player_one.all_cards) < 5):
                    print('Player one is unable to play with 5 cards')
                    print('Player two wins the game')
                    game_on = False
                    break
                elif (len(player_two.all_cards) < 5):
                    print('Player two is unable to play with 5 cards')
                    print('Player one wins the game')
                    game_on = False
                    break
                else:
                    for i in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

        rounds += 1


if __name__ == '__main__':
    run_game()
