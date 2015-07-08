from player import Player
from dealer import Dealer
from deck import Deck
from display import Display


class Game():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.display = Display(8)
        self.pot = 0

    def print_display(self, wait=False):
        self.update_display()
        self.display.print_display()
        if wait:
            self.get_continue()

    def update_display(self, hidden=True):
        display_list = ["Dealer:", self.dealer.display_hand(),
                        "Score: " + str(self.dealer.get_hand_value()) +
                        " | Pot: " + str(self.pot),
                        "- "*20, "You:", self.player.display_hand(),
                        "Score: " + str(self.player.get_hand_value()) +
                        " | Money: " + str(self.player.score)]
        for index, string in enumerate(display_list):
            self.display.set_display(string, index)

    def start_round(self):
        self.deck = Deck()
        self.player.start_game()
        self.dealer.start_game()
        self.add_message("Welcome to Blackjack!")
        self.print_display(True)
        self.pot = self.player.bet(self.get_input("bet"))
        self.initial_deal()
        if self.dealer.has_blackjack() and self.player.has_blackjack():
            self.dealer.hidden = False
            self.push("Both dealer and player have Blackjack.")
            return self.get_input("hand")
        elif self.player.has_blackjack():
            self.player_wins("You have Blackjack!")
            return self.get_input("hand")
        elif self.dealer.has_blackjack():
            self.dealer.hidden = False
            self.dealer_wins("Dealer has Blackjack.")
            return self.get_input("hand")
        return self.play()

    def initial_deal(self):
        for i in range(2):
            self.player.add_card(self.deal())
            self.print_display(True)
            self.dealer.add_card(self.deal())
            self.print_display(True)

    def get_input(self, type):
        self.print_display()
        if type == "hand":
            return self.get_hand_input()
        elif type == "bet":
            return self.get_bet_input()
        elif type == "choice":
            return self.get_stand_or_hit()

    def get_hand_input(self):
        if not self.enough_money():
            return False
        while True:
            string = "Do you want to play another hand? (y/n) > "
            value = input(string).lower()
            if value in ("y", "n"):
                return value
            self.add_message("Please enter 'y' or 'n'")
            self.print_display()

    def get_bet_input(self):
        while True:
            bet = input("How much do you want to bet? > ")
            if bet.isdigit() and bet != "0":
                if int(bet) > self.player.score:
                    self.add_message("You don't have that much.")
                    self.print_display()
                    continue
                return int(bet)
            self.add_message("Please enter a positive integer.")
            self.print_display()

    def get_stand_or_hit(self):
        while True:
            string = "Do you want to stand, hit, or double down? > "
            value = input(string).lower()
            if value in ("stand", "hit", "double down"):
                return value
            self.add_message("Please enter 'stand', 'hit', or 'double down'.")
            self.print_display()

    def add_message(self, message):
        self.display.add_messages(message)

    def get_continue(self):
        input("Press Enter to continue.")

    def deal(self):
        return self.deck.draw()

    def player_play(self):
        while True:
            choice = self.get_input("choice")
            if choice == "hit":
                self.player.add_card(self.deal())
                if self.player.has_blackjack():
                    self.add_message("You have Blackjack!")
                    self.print_display(True)
                    return True
                elif self.player.is_busted():
                    self.add_message("You have busted.")
                    self.print_display(True)
                    return False
                continue
            if choice == "double down":
                if self.player.score < self.pot:
                    self.add_message("You don't have enough money.")
                    self.print_display(True)
                    continue
                self.add_message("Doubling down.")
                self.pot += self.player.bet(self.pot)
                self.print_display(True)
                self.player.add_card(self.deal())
                if self.player.has_blackjack():
                    self.add_message("You have Blackjack!")
                    self.print_display(True)
                    return True
                elif self.player.is_busted():
                    self.add_message("You have busted.")
                    self.print_display(True)
                    return False
            return True

    def dealer_play(self):
        self.dealer.start_turn()
        self.print_display(True)
        while self.dealer.get_hand_value() < 17:
            self.add_message("Dealer hits.")
            self.dealer.add_card(self.deal())
            if self.dealer.has_blackjack():
                self.add_message("Dealer has Blackjack.")
                self.print_display(True)
                return
            if self.dealer.is_busted():
                self.add_message("Dealer is busted!")
                self.print_display(True)
                return
            self.print_display(True)
        self.add_message("Dealer stands.")
        self.print_display(True)

    def play(self):
        if self.player_play():
            self.dealer_play()
        if self.dealer.get_hand_value() == self.player.get_hand_value():
            self.push()
        elif self.dealer.is_busted() or self.player.has_blackjack():
            self.player_wins()
        elif self.dealer.has_blackjack() or self.player.is_busted():
            self.dealer_wins()
        elif self.player.get_hand_value() > self.dealer.get_hand_value():
            self.player_wins()
        else:
            self.dealer_wins()
        return (self.get_input("hand") == "y")

    def run(self):
        while self.start_round():
            pass
        return True

    def player_wins(self, message=""):
        if message:
            self.add_message(message)
        self.add_message("You win the hand!")
        self.print_display(True)
        pot_multiplier = 2
        if self.player.has_blackjack():
            pot_multiplier = 3
        self.add_message("You won {}!".format(self.pot * pot_multiplier))
        self.player.add_score(self.pot * pot_multiplier)
        self.pot = 0
        self.print_display(True)

    def dealer_wins(self, message=""):
        if message:
            self.add_message(message)
        self.add_message("You lose the hand.")
        self.print_display(True)
        self.pot = 0

    def push(self, message=""):
        if message:
            self.add_message(message)
        self.add_message("The round is a push.")
        self.print_display(True)

    def enough_money(self):
        if self.player.score < 1:
            self.add_message("You don't have enough money to continue.")
            self.add_message("Thank you for playing.")
            self.print_display(True)
            return False
        return True
