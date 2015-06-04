
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


#    def __init__(self):
        # self.RANK = RANK
        # self.SUIT = SUIT
        # self.p_dict = p_dict
    # def e_list(self):
        # return [[] for x in xrange(0, self.RANK)]

    """def point_dict(self):
        for i in self.RANK:
            if int(i) is True:
                p_dict[i] = int(i)
            elif i == 'ace':
                p_dict[i] = 11
            else:
                p_dict[i] = 10
        return p_dict"""
