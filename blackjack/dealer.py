from player import Player


class Dealer(Player):
    def __init__(self):
        pass

    def display_hand(self, hidden=False):
        return self.hand.card_list_display(hidden)

    def bet(self):
        pass

    def add_score(self):
        pass

    def get_hand_value(self, hidden=False):
        return self.hand.get_score(hidden)
