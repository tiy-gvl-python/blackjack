class Card():
    def __init__(self, suit, rank):
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __repr__(self):
        return "{} of {}".format(self.rank.title(), self.suit.title())

if __name__ == "__main__":
    test_list = [("hearts", "king"), ("diamonds", "2")]
    card_list = [Card(suit, rank) for suit, rank in test_list]
    assert card_list[0].suit == "hearts"
    assert card_list[1].suit == "diamonds"
    assert card_list[0].rank == "king"
    assert card_list[1].rank == "2"
    assert str(card_list[0]) == "King of Hearts"
    assert str(card_list[1]) == "2 of Diamonds"
