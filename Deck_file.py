import random
import itertools


class Deck:
    def remove_from_deck(self, remove):
        try:
            self.deck.remove(remove[0])
            self.deck.remove(remove[1])
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
        self.hand = random.sample(self.deck, 2)
        self.deck = self.remove_from_deck(self.hand)
        print("This is your hand", self.hand)
        return (self.hand)

    def hitme(self):
        self.deal = random.choice(self.deck)
        self.hand.append(self.deal)
        print("This is your hand", self.hand)

    def ask(self):
        self.hit_me_or = input("Hit me? or Stay? ")
        self.hit_me_or.lower()
        if self.hit_me_or == "hit me":
            self.hitme()
        elif self.hit_me_or == "stay":
            pass
        else:
            print("Hit me or Stay")
            self.ask()
