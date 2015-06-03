import random
import itertools


class Deck:
    def remove_from_deck(self, deck, remove):
        # print(deck)
        # print(remove)
        self.dec = deck
        try:
            # print(self.dec)
            self.dec.remove(remove[0])
            # print(self.dec)
            self.dec.remove(remove[1])
            # print(self.dec)
            return self.dec
        except:
            # self.dec.remove(remove[0])
            # print(self.dec)
            return self.dec

    def shuffle(self):
        self.suits = 'cdhs'
        self.rank = '23456789TJQKA'
        # print(list(itertools.product(suits, rank)))
        self.deck = tuple(''.join(card) for card in itertools.product(
            self.suits, self.rank))

        self.deck = list(self.deck)
        return self.deck

    def init_deal(self, deck):
        # print(deck)
        self.hand = random.sample(deck, 2)
        # print(self.hand)
        # print(self.deck)
        self.deck = Deck.remove_from_deck(self, deck, self.hand)
        # print(self.deck)
        return (self.hand, self.deck)

    def hitme(self, tuple):
        # print("Tuple", tuple)
        self.hand = tuple[0]
        # print("Type", type(self.hand))
        self.deck = tuple[1]
        self.deal = random.choice(self.deck)
        # print("Random Deal", self.deal)
        # print("Type Now", type(self.hand))
        # print(self.hand)
        self.hand.append(self.deal)
        # print(self.hand)
        self.deck = Deck.remove_from_deck(self, self.deck, self.deal)
        return (self.hand, self.deck)

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
