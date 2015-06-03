import Deck_file
from Deck_file import Deck
import Card_file
from Card_file import Card

new_deck = Deck()
new_card = Card()
shuffled = new_deck.shuffle()


def test_init_deck(shuffled):
    # print(shuffled)
    # print(new_deck.init_deal(shuffled))
    try:
        assert len(new_deck.init_deal(shuffled)[0]) == 2
        assert len(new_deck.init_deal(shuffled)[0][0]) == 2
        return new_deck.init_deal(shuffled)
    except:
        print("init_deal isn't working")


def test_init_hitme(tuple):
    try:
        assert len(tuple) == 2
        assert len(tuple[0]) == 3
    except:
        print("Hit Me isnt working")


def test_card(hand):
    try:
        assert new_card.count(hand) == "lose"
    except:
        print("Card.count isnt working")

# new_deck.hitme(new_deck.init_deal(shuffled))
test_init_deck(shuffled)
test_init_hitme(new_deck.hitme(new_deck.init_deal(shuffled)))
test_card(['cT', 'A', 'd6'])
