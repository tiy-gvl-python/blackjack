from hand import Hand


class Player():
    def __init__(self):
        self.score = 100

    def start_game(self):
        self.deck = Hand()

    def end_game(self):
        pass

    def add_card(self, card):
        self.deck.add_card(card)

    def is_busted(self):
        return self.deck.busted

    def has_blackjack(self):
        return self.deck.blackjack

    def has_soft_hand(self):
        return self.deck.soft

    def bet(self, amount=10):
        self.score -= amount
        return amount

    def add_score(self, amount):
        self.score += amount

    def get_hand_value(self):
        return self.hand.

    @property
    def display_hand(self):
        return self.hand.card_list_display()
