import Deck_file
from Deck_file import Deck
import Card_file
from Card_file import Card

new_deck = Deck()
new_card = Card()
new_deck.shuffle()


def test_init_deck():
    try:
        assert len(new_deck.init_deal()) == 2
        assert len(new_deck.init_deal()[0]) == 2
        return new_deck.init_deal()
    except:
        print("init_deal isn't working")


def test_init_hitme(hand):
    try:
        assert len(hand) == 3
        assert len(hand[0]) == 2
    except:
        print("Hit Me isnt working")


def test_card(hand):
    try:
        print("Enter 11 for test")
        assert new_card.count(hand) == "lose"
    except:
        print("Card.count isnt working")

# new_deck.hitme(new_deck.init_deal(shuffled))
test_init_deck()
test_init_hitme(new_deck.hitme())
test_card(['cT', 'A', 'd6'])
