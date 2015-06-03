import random
from card import Card


class Deck():
    def __init__(self):
        self.create_card_list()
        self.shuffle()

    @property
    def card_list(self):
        return self._card_list

    def shuffle(self):
        random.shuffle(self._card_list)

    def draw(self):
        return self._card_list.pop()

    def create_card_list(self):
        numbers = list(map(str, range(2, 11)))
        ranks = ['ace', 'king', 'queen', 'jack']
        ranks.extend(numbers)
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self._card_list = [Card(suit, rank)
                           for rank in ranks for suit in suits]

    @property
    def card_list_display(self):
        return '\n'.join(map(str, self._card_list))

if __name__ == "__main__":
    test_deck = Deck()
    example_card = Card("hearts", "3")
    assert len(test_deck.card_list) == 52
    assert type(test_deck.draw()) == type(example_card)
    assert len(test_deck.card_list) == 51
