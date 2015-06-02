class Card():
    def __init__(self, suit, rank):
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __repr__(self):
        return "{} of {}".format(self.rank.title(), self.suit.title())
