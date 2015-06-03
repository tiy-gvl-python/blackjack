"""
The Hand class will keep a collection of cards.  It will use the rules to
determine the value of that hand.  It will contain a boolean to keep track of
whether the hand is busted, and it will contain another boolean to keep track
of whether the hand is blackjack.  It will have a method that will be used to
add cards to the hand.
"""
class Hand():
    def __init__(self):
        self._card_list = []
        self.score = 0
        self.blackjack = False
        self.busted = False

    @property
    def card_list(self):
        return self.card_list

    def get_score(self):
        return sum([card.value for card in card_list])

    def start_card_value(self, rank):
        if not card.rank.isalpha() and card.rank != "ace":
            return int(card.rank)
        elif card.rank != "ace":
            return 10
        self.soft = True
        return 11

    def reevaluate_score(self):
        if self.get_score() > 21:
            for card in self._card_list:
                if card.rank == "ace" and card.value == 11:
                    card.value = 1
                    break
        elif self.get_score == 21:
            self.blackjack = True
            return
        if self.get_score() > 21:
            self.busted = True

    def add_card(self, card):
        card.value = self.start_card_value(card.rank)
        self._card_list.append(card)
        self.reevaluate_score()

    @property
    def card_list_display(self, show_all=True):
        card_list = self.card_list
        if not show_all:
            card_list[0] = ""
        return ", ".join(card_list)
