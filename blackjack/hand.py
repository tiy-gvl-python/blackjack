from card import Card


class Hand():
    def __init__(self):
        self._card_list = []
        self.score = 0
        self.blackjack = False
        self.busted = False
        self.soft = False

    @property
    def card_list(self):
        return [card for card in self._card_list]

    def get_score(self, hidden=False):
        for card in self.card_list:
            print(card)
        if hidden:
            return 0
        return sum([card.value for card in self.card_list])

    def start_card_value(self, rank):
        if not rank.isalpha() and rank != "ace":
            return int(rank)
        elif rank != "ace":
            return 10
        self.soft = True
        return 11

    def evaluate_score(self):
        if self.get_score() > 21:
            for card in self.card_list:
                if card.rank == "ace" and card.value == 11:
                    card.value = 1
                    self.soft = False
                    break
        if 11 in [card.value for card in self.card_list]:
            self.soft = True
        if self.get_score() == 21:
            self.blackjack = True
            return
        if self.get_score() > 21:
            self.busted = True
            self.blackjack = False

    def add_card(self, card):
        card.value = self.start_card_value(card.rank)
        print(card.value)
        self._card_list.append(card)
        self.evaluate_score()

    def card_list_display(self, hidden=False):
        card_list = self.card_list
        if hidden and card_list:
            card_list[0] = Card("Cards", "Unknown")
        return ", ".join(map(str, card_list))

if __name__ == "__main__":
    from card import Card
    test_hand = Hand()
    test_hand.add_card(Card("Spades", "Ace"))
    assert test_hand.get_score() == 11
    test_hand.add_card(Card("Clubs", "Ace"))
    assert test_hand.get_score() == 12
    test_hand.add_card(Card("Diamonds", "5"))
    assert test_hand.get_score() == 17
    assert test_hand.soft
    assert not test_hand.blackjack
    assert not test_hand.busted
    test_hand.add_card(Card("Hearts", "Queen"))
    assert test_hand.get_score() == 17
    test_hand.add_card(Card("Hearts", "4"))
    assert test_hand.get_score() == 21
    assert not test_hand.soft
    assert not test_hand.busted
    assert test_hand.blackjack
    test_hand.add_card(Card("Clubs", "Jack"))
    assert test_hand.busted
    assert not test_hand.blackjack
    assert not test_hand.soft
    assert test_hand.get_score() == 31
