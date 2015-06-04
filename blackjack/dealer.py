from player import Player


class Dealer(Player):
    def __init__(self):
        del self.bet
        del self.add_score

    @property
    def display_hand(self):
        return self.hand.card_list_display(False)
