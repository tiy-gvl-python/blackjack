from hand import Hand


class Player():
    def __init__(self):
        self.score = 100

    def start_game(self):
        self.hand = Hand()

    def end_game(self):
        pass

    def add_card(self, card):
        self.hand.add_card(card)

    def is_busted(self):
        return self.hand.busted

    def has_blackjack(self):
        return self.hand.blackjack

    def has_soft_hand(self):
        return self.hand.soft

    def bet(self, amount=10):
        self.score -= amount
        return amount

    def add_score(self, amount):
        self.score += amount

    def get_hand_value(self):
        return self.hand.get_score(False)

    def display_hand(self):
        return self.hand.card_list_display(False)
