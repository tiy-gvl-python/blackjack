import Deck_file
from Deck_file import Deck
import Card_file
from Card_file import Card
import Dealer_file
from Dealer_file import Dealer

new_dealer = Dealer
new_deck = Deck()
new_card = Card()

new_deck.shuffle()
new_deck.init_deal()
while True:
    new_deck.ask()
    print(new_deck.hand)
    new_card.count(new_deck.hand)
