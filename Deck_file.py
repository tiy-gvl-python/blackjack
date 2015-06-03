import random
import itertools
import Card


class Deck:
    def init_deal(self):
        self.suits = 'cdhs'
        self.rank = '23456789TJQKA'
        # print(list(itertools.product(suits, rank)))
        self.deck = tuple(''.join(card) for card in itertools.product(self.suits, self.rank))
        self.deck = list(self.deck)
        self.hand = random.sample(self.deck, 2)
        # print(self.hand)
        self.deck.remove(self.hand[0])
        self.deck.remove(self.hand[1])
        # print(self.deck)
        return self.hand

    def hitme(self):
        self.deal = random.choice(self.deck)
        self.deck.remove(self.deck)
        return self.deal

    def check_16(self):
        if check_hand(self) == 16:
            return False

    def ask(self):
        self.hit_me_or = input("Hit me? or Stay?")
        self.hit_me_or.lower()
        if self.hit_me_or == "hit me":
            hitme(self)
        elif self.hit_me_or == "stay":
            pass
        else:
            print("Hit me or Stay")
            ask(self)
