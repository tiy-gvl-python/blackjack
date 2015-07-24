import random
import os
os.system("clear")


class Card:

    def __init__(self, value, suite=None):
        self.value = value
        self.suite = suite

    def __str__(self):
        return self.value


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        return sum([card.number for card in self.cards])

    def hand_value(self):
        return sum(self.hand)

    def hit_or_stay(self):



class