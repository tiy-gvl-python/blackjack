import random


class Deck():

    def __init__(self, hand):
        self.card_dict = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5,
                          "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                          "King": 10, "Queen": 10}
        self.card()
        self.card_value()
        self.hand = hand
        self.shuffle()
        self.deal_comp()
        self.deal_play()

    def card(self):
        self.deck = list(self.card_dict.keys()) * 4

    def card_value(self):
        self.deck_value = list(self.card_dict.values()) * 4

    def shuffle(self):
        random.shuffle(self.deck_value)

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
        self.sum_comp()
        self.sum_play()

    def sum_comp(self):
        self.sum_computer = sum(self.computer_hand)

    def sum_play(self):
        self.sum_player = sum(self.player_hand)

    def clear_play_hand(self):
        del self.player_hand[:]

    def clear_comp_hand(self):
        del self.computer_hand[:]


class Dealer():

    def __init__(self, hand, deck):
        self.hand = hand
        self.deck = deck

    def hit_logic(self):
        while True:
            self.deck.shuffle()
            self.deck.deal_comp()
            self.hand.sum_comp()
            if self.hand.sum_computer >= 16:
                break
            else:
                continue

    def stand_logic(self):
        if self.hand.sum_computer >= 16 and self.hand.sum_computer < 22:
            stand = True
        else:
            stand = False


class Player():

    def __init__(self, hand, deck, dealer):
        self.hand = hand
        self.deck = deck
        self.dealer = dealer

    def choose_logic(self):
        while True:
            self.deck.shuffle()
            self.deck.deal_play()
            print(self.hand.player_hand)
            x = input("Press H to hit or something else to stand.")
            if x == "H":
                continue
            else:
                break


class Game():

    def __init__(self, hand, deck, dealer, player):
        self.hand = hand
        self.deck = deck
        self.dealer = dealer
        self.player = player

    def game_logic(self):
        x = True
        stand = None
        while x == True:
            deck.card_value()
            dealer.hit_logic()
            dealer.stand_logic()
            player.choose_logic()
            if hand.computer_hand >= hand.player_hand:
                print('computer wins!')
                print(hand.computer_hand)
                print(hand.player_hand)
                x = False
            else:
                print('player wins!')
                print(hand.computer_hand)
                print(hand.player_hand)
                x = False

hand = Hand()
deck = Deck(hand)
dealer = Dealer(hand, deck)
player = Player(hand, deck, dealer)
game = Game(hand, deck, dealer, player)
game.game_logic()
