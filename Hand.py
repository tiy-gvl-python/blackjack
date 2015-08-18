import Deck_file
from Deck_file import Deck
import Card_file
from Card_file import Card
import Dealer_file
from Dealer_file import Dealer


class Hand:
    new_deck = Deck()
    new_deck.shuffle()
    self.dealer_hand = new_deck.init_deal()

    def player_going:
        new_deck.ask()
    self.player_hand = new_deck.init_deal()
