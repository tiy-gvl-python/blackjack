import Deck_file
from Deck_file import Deck
import Card_file
from Card_file import Card
import Dealer_file
from Dealer_file import Dealer
import random
# import Hand
# from Hand import Hand

new_card = Card()
new_dealer = Dealer()
new_deck = Deck()
new_deck.shuffle()
new_deck.init_deal()

while True:
    dealer = random.random()
    new_deck.ask()
    new_card.count(new_deck.hand, "player")

    print("Your card add up to ", new_card.counter)
    if dealer >= .5:
        new_deck.hitme("dealer")
    if dealer < .5:
        print("Dealer Stayed")

    new_card.count(new_deck.dealer_hand, "dealer")
    print("Your dealer card add up to ", new_card.counter)
