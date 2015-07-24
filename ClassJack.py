import random
import os

os.system("clear")

# classes
class PlayerHand:
    def __init__(self):
        self.player_hand = []

    def __str__(self):
        return self.player_hand


class DealerHand:
    def __int__(self):
        self.dealer_hand = []

    def __str__(self):
        return self.dealer_hand


# functions
def setup_deck(deck, money):
    print("Let's play some Blackjack")
    print("\n")
    money -= 10
    print("You currently have ${} and each play will cost $10".format(money))
    print("\n")
    print("Hit = 'H', and Pass = 'P'")
    return







def get_new_card(player_hand, dealer_hand):
    live_card = Cards.pop()
    # print("{} cards left in deck".format(len(deck)))
    # print(live_card)
    return(live_card)


def win_lose():
    if win:
        bankroll += 10
        print("You win")
    else:
        print("Better luck next time")
        print("Your have {}".format(bankroll))








def deal(player_hand, dealer_hand):
    counter = 0
    while counter < 2:
        player_hand.append(get_new_card(player_hand, dealer_hand))
        dealer_hand.append(get_new_card(player_hand, dealer_hand))
        counter += 1
    print("{} : Your hand".format(player_hand))
    print("{} : Secret dealer hand for testing".format(dealer_hand))


def player_hit_pass(player_hand):
    player_input = input("'H'it or 'P'ass?").upper()
    if player_input == "P":
        return sum(player_hand)

    else:
        player_hand.append(get_new_card(player_hand, dealer_hand))
        print("{} : Your hand".format(player_hand))
    print("\n")

    print(input("OK, hit ENTER for dealer's turn"))

player_hand =






deal (player_hand, dealer_hand)
print("\n")
print("\n")
player_hit_pass(player_hand)







'''
class Cards:
    def __init__(self):
        self.deck = ['A of clubs', 'K of clubs', 'Q of clubs', 'J of clubs',
                     '10 of clubs', '9 of clubs', '8 of clubs', '7 of clubs',
                     '6 of clubs', '5 of clubs', '4 of clubs', '3 of clubs',
                     '2 of clubs', 'A of hearts', 'K of hearts', 'Q of hearts',
                     'J of hearts', '10 of hearts', '9 of hearts', '8 of hearts',
                     '7 of hearts', '6 of hearts', '5 of hearts', '4 of hearts',
                     '3 of hearts', '2 of hearts', 'A of diamonds', 'K of diamonds',
                     'Q of diamonds', 'J of diamonds', '10 of diamonds',
                     '9 of diamonds', '8 of diamonds', '7 of diamonds',
                     '6 of diamonds', '5 of diamonds', '4 of diamonds',
                     '3 of diamonds', '2 of diamonds', 'A of spades', 'K of spades',
                     'Q of spades', 'J of spades', '10 of spades', '9 of spades',
                     '8 of spades', '7 of spades', '6 of spades', '5 of spades',
                     '4 of spades', '3 of spades', '2 of spades']

    @property
    def __str__(self):
        return random.shuffle(self.deck)
'''

'''
class Dealer:
    def __init__(self):
        self.player = player_1
        self.dealer = dealer
'''

'''
class Bankroll:
    def __init__(self):
        self.bank = 100
        self.play = 10

    def pay_to_play(self):
        if self.bank <= 0
            return
        else:
            self.bank -= self.play
'''
