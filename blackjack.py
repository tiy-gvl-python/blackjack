import random

class Cards():
    face = list(range(2,11)) + "Jack Queen King Ace".split()
    suits = "Diamonds Clubs Hearts Spades".split()


class Deck():
    # list comprehension takes from face and suits and asigns all faces to each suit
    ordered = [["{0} of {1}".format(fv, s)] for fv in Cards.face for s in Cards.suits]

    # second list comprehenison holds value here
    # dont think this is neccassary but im tired and its not throwing any errors
    deck = [x for x in ordered]
    shuffled_deck = random.sample(deck, 52)





class Player():
    player_hand = []

    player_points = 0

    def __init__(self):
        self.player_hand = player_hand
        self.player_points = player_points
        pass

    def __str__(self):
        return "Your cards: {} \n Your points: ".format(self.player_hand, self.player_points)


    def player_hand(self):
        self.player_hand = player_hand


    def player_rules(self, player_hand):

        face = Cards.face

        for card in self.player_hand:
            if "Ace" in card:
                ace_decision = input("You have an ace please enter 1 or 11 ")
                while ace_decision != 1 or 11:
                    ace_decision = input("Please enter 1 or 11 you drunk bastard. ")
                self.player_points = self.player_points + ace_decision
            elif "Jack" or "Queen" or "King" in self.player_hand:
                self.player_points = self.player_points + 10
            elif range(face(2,11)) in self.player_hand:
                self.player_points = self.player_points + int(player_hand[0])
        return self.player_points





class Dealer():
    face = Cards.face
    dealer_hand = []
    dealer_points = 0


    def __init__(self):
        self.dealer_hand = dealer_hand
        self.dealer_points = dealer_points

    def __str__(self, dealer_hand, dealer_points):
        return "Dealers card: {}" + dealer_hand.index(0)

    def dealer_rules(self):
        for card in self.dealer_hand:
            if "Ace" in card:
                if self.dealer_points <= 10:
                    self.dealer_points + 11
                else:
                    self.dealer_points + 1
            elif "Jack" or "Queen" or "King" in card:
                self.dealer_points + 10
            elif range(face(2,11)) in card:
                self.dealer_points = self.dealer_points + int(card[0])






class Game:

    game_deck = Deck.shuffled_deck

    new_game = False

    def __init__(self):

        self.player = Player()
        self.dealer = Dealer()

    def start_game(self):
        self.new_game = True
        self.dealer.dealer_hand = self.dealer.dealer_hand.append(self.game_deck.pop()+self.game_deck.pop())
        self.player.player_hand = self.player.player_hand.append(self.game_deck.pop()+self.game_deck.pop())

    def hit_or_stay(self):
        self.player_points = self.player.player_points
        self.dealer_points = self.dealer.dealer_points

        while self.dealer_points <= 16:
            self.dealer.dealer_hand = self.dealer.dealer_hand + self.game_deck.pop()

        while self.player_points <= 21:


            



    def end_game(self):
        pass








