
import random


class Deck():
    RANK = ['2', '3', '4', '5', '6', '7', '8', '9', 'ten', 'jack', 'queen', 'king', 'ace']
    SUIT = [' of clubs', ' of hearts', ' of spades', ' of diamonds']
    deck_list = []
    # Should this be a function?

    for i in RANK:
        deck_list.append(i + SUIT[0])
        deck_list.append(i + SUIT[1])
        deck_list.append(i + SUIT[2])
        deck_list.append(i + SUIT[3])
