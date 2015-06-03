import Deck_file
from Deck_file import Deck


class Tests:
    "Tests"
    def test_init_deck(self):
        self.new_deck = Deck()
    # print(len(new_deck.init_deal()[0]))
        try:
            assert len(self.new_deck.init_deal()) == 2
            assert len(self.new_deck.init_deal()[0]) == 2
        except:
            print("init_deal isn't working")

print(Tests.test_init_deck())
