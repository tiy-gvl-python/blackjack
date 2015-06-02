import random
from card import Card


class Deck():
    def __init__(self):
        numbers = list(map(str, range(2, 11)))
        ranks = ['ace', 'king', 'queen', 'jack']
        ranks.extend(numbers)
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self.card_list = [Card(suit, rank) for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.card_list)

    def __repr__(self):
        return str(self.card_list)

    def deal(self):
        return self.card_list.pop()


deck = Deck()
print(deck)
print(deck.deal())
print(deck)
