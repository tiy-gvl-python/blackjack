from player import Player
from hand import Hand


class Dealer(Player):
    def __init__(self):
        self.hidden = True

    def display_hand(self):
        return self.hand.card_list_display(self.hidden)

    def bet(self):
        pass

    def add_score(self):
        pass

    def get_hand_value(self):
        return self.hand.get_score(self.hidden)

    def start_game(self):
        self.hidden = True
        self.hand = Hand()

    def start_turn(self):
        self.hidden = False
