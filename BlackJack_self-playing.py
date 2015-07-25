import random
import os


class Deck:
    def __init__(self, deck):
        self.deck = deck


class Player:
    def __init__(self, deck):
        self.hand = []
        self.money = 100
        self.deck = deck

    def draw_card(self):
        self.hand.append(random.choice(self.deck.deck))

    def hand_value(self):
        if 1 in self.hand:
            if 7 <= sum(self.hand) <= 11:
                return sum(self.hand) + 10
        return sum(self.hand)

    def dealer_hit_or_stay(self):
        for _ in range(10):
            if self.hand_value() < 17:
                self.draw_card()

    def player_hit_or_stay(self):
        choice = input("Enter 'h' to Hit or just 'Enter' to Stay. ").lower()
        if choice == 'h':
            self.draw_card()
            self.player_hit_or_stay()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    def begin_game(self):
        import os
        os.system("clear")

        print ("Player has ${} to play with:".format(player1.money))
        print("Dealing cards...")
        for _ in range(2):
            player1.draw_card()
            player2.draw_card()
        if player1.hand_value() == 21:
            if player2.hand_value() == 21:
                print("Player and Dealer have BlackJack!")
                print("Game is a tie")
                print("Player hand ", player1.hand)
                print("Dealer hand ", player2.hand)
                print("Player funds = $", player1.money)
                self.play_again()
            print("Player wins with BlackJack!")
            print("Player hand ", player1.hand)
            print("Dealer hand ", player2.hand)
            player1.money += 10
            print("Player funds = $", player1.money)
            self.play_again()
        elif player2.hand_value() == 21:
            print("Dealer wins with BlackJack!")
            print("Player hand ", player1.hand)
            print("Dealer hand ", player2.hand)
            player1.money -= 10
            print("Player funds = $", player1.money)
            self.play_again()
        else:
            print("Player hand ", player1.hand)
            print("Dealer is showing a [{}]".format(player2.hand[0]))
            game.game_continue()

    def game_continue(self):
        player1.dealer_hit_or_stay()
        player2.dealer_hit_or_stay()
        game.winner()

    def play_again(self):
        play_choice = input("Play again? Enter 'Y'es or just Enter to quit").lower()
        if play_choice == 'y':
            player1.hand = []
            player2.hand = []
            game.begin_game()
        else:
            print("Your final dollar amount is ${}".format(player1.money))
            #return


    def winner(self):
        if player1.hand_value() > 21:
            player1.money -= 10
            print("Player has gone bust")
            if player2.hand_value() > 21:
                print("Dealer has also gone bust")
                player1.money += 10
                print("Player has ${}".format(player1.money))
                game.show_cards()
                return
            print("Player has ${}".format(player1.money))
            game.show_cards()
        elif player2.hand_value() > 21:
            player1.money += 10
            print("Dealer has gone bust.  Player wins")
            print("Player has ${}".format(player1.money))
            game.show_cards()
        elif player1.hand_value() > player2.hand_value():
            player1.money += 10
            print("Player is the winner with a score of {}.".format(self.player1.hand_value()))
            print("Player has ${}".format(player1.money))
            game.show_cards()
        elif player2.hand_value() > player1.hand_value():
            player1.money -= 10
            print("Dealer is the winner with a score of {}.".format(self.player2.hand_value()))
            print("Player has ${}".format(player1.money))
            game.show_cards()
        else:
            print("It's a tie.  Player {} / Dealer {}".format(self.player1.hand_value(), self.player2.hand_value()))
            game.show_cards()

    def show_cards(self):
        print("Player hand ", player1.hand, "total score", player1.hand_value())
        print("Dealer hand ", player2.hand, "total score", player2.hand_value())
        if player1.money == 0:
            print("Sorry, you are out of money.  You'll have to start the game again.")
            return
        else:
            game.play_again()

deck = Deck(deck=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
player1 = Player(deck)
player2 = Player(deck)
game = Game(player1, player2)
game.begin_game()
