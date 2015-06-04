from player import Player
from dealer import Dealer
from deck import Deck
from display import Display


class Game():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.display = Display()

    def print_display(self):
        self.display.print_display()

    def start_round(self):
        self.deck = Deck()
        self.player.bet(self.get_bet_input())

    def get_play_input(self):
        while input("Do you want to play again? (y/n) > ").lower()\
                not in ("y", "n"):
            print("Please enter 'y' or 'n'")

    def get_bet_input(self):
        # return input("How much do you want to bet?")
        print("Betting 10.")
        return 10

    def get_stand_or_hit()
