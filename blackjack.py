import random


class Deck():

    def __init__(self, hand):
        self.card_dict = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "King": 10, "Queen": 10}
        self.card()
        self.card_value()
        self.hand = hand
        self.shuffle()
        self.deal_comp()
        self.deal_play()

    def card(self):
        self.deck = list(self.card_dict.keys()) * 4
        print(self.deck)

    def card_value(self):
        self.deck_value = list(self.card_dict.values()) * 4
        print(self.deck_value)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_comp(self):
        self.hand.computer_hand.append(self.deck_value[1])

    def deal_play(self):
        self.hand.player_hand.append(self.deck_value[0])


class Hand():

    def __init__(self):
        self.computer_hand = []
        self.player_hand = []
        self.clear_play_hand()
        self.clear_comp_hand()

    def sum_hand(self):
        self.sum_computer = sum(self.computer_hand)
        self.sum_player = sum(self.player_hand)

    def clear_play_hand(self):
            del self.player_hand[:]

    def clear_comp_hand(self):
            del self.computer_hand[:]


class Dealer():

    def __init__(self, hand, deck, player):
        self.hand = hand
        self.deck = deck
        self.player = player

    def hit_logic(self):
        hit is True
        while hit is True:
            self.shuffle()
            self.deal_comp()
            if self.sum_computer > 16:
                hit is False

    def stand_logic(self):
        stand is False
        if self.sum_computer > 16 and < 22:
            stand is True


class Player():

    def __init__(self, hand, deck, dealer):
        self.hand = hand
        self.deck = deck
        self.dealer = dealer

    def choose_logic(self):
        choose = raw_input("Press H to hit or S to stand.")
        if choose = "h" or "H":
            self.shuffle()
            self.deal_play()
            print(self.player_hand)
        else:
            stand is True

class Game():

    




player = Player()
dealer = Dealer(hand)
hand = Hand()
deck = Deck(hand)
