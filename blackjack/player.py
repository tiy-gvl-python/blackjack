from hand import Hand

class Player():
    def __init__(self):
        self.score = 100

    def start_game(self):
        self.deck = Hand()

    def add_card(self, card):
        self.deck.add_card(card)

    def is_busted(self):
        return self.deck.busted

    def has_blackjack(self):
        return self.deck.blackjack

    def has_soft_hand(self):
        return self.deck.soft
