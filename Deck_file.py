import random
import itertools


class Deck:
    # deck = shuffle()
    def remove_from_deck(self, remove):
        # print(deck)
        # print(remove)
        try:
            # print(self.dec)
            self.deck.remove(remove[0])
            # print(self.dec)
            self.deck.remove(remove[1])
            # print(self.dec)
            return self.deck
        except:
            pass

    def shuffle(self):
        self.suits = 'cdhs'
        self.rank = '23456789TJQKA'
        self.deck = list(''.join(card) for card in itertools.product(
            self.suits, self.rank))
        return self.deck

    def init_deal(self):
        # print(deck)
        # print("i'm here", self.deck)
        self.hand = random.sample(self.deck, 2)
        # print(self.hand)
        # print("now i'm here", self.deck)
        self.deck = self.remove_from_deck(self.hand)
        # print("and now i'm here", self.deck)
        # print(self.deck)
        return (self.hand)

    def hitme(self):
        print(self.deck)
        self.deal = random.choice(self.deck)
        # print("Random Deal", self.deal)
        # print("Type Now", type(self.hand))
        # print(self.hand)
        self.hand.append(self.deal)
        # print(self.hand)
        # self.deck = Deck.remove_from_deck(self, self.deck, self.deal)
        return (self.hand)

    def check_16(self):
        if check_hand(self.hand) == 16:
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
