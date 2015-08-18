import Deck_file
from Deck_file import Deck


def test_init_deck():
    new_deck = Deck()
    # print(len(new_deck.init_deal()[0]))
    try:
        assert len(new_deck.init_deal()) == 2
        assert len(new_deck.init_deal()[0]) == 2
    except:
        print("init_deal isn't working")


def test_init_hitme():
    hitme = hitme()
    try:
        assert len(hitme.hitme()) == 1
        assert len(hitme.hitme()[0]) == 2
    except:
        print("init_deal isn't working")

test_init_deck()
test_init_hitme()
