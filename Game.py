import Deck_file
from Deck_file import Deck
import Card_file
from Card_file import Card
import Dealer
from Dealer import Dealer

new_dealer = Dealer
new_deck = Deck()
new_card = Card()
new_deck.shuffle()

new_deck.init_deal()
test_init_hitme(new_deck.hitme())
test_card(['cT', 'A', 'd6'])
