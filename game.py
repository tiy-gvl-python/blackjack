import random
import re
from blackjack import Hand
from blackjack import Deck


def card_pick(a_deck):
    return a_deck.pop(random.randrange(len(a_deck)))


def dealer_protocol(hand, deck):
    while Hand.Hand.hand_check(hand) < 17:
            hand.append(card_pick(deck))
    return hand

#  a = ['jack of hearts', 'queen of spades']
#  print(hand_check(a))


def game():
    deck = Deck.Deck.deck_list
    p_hand = [card_pick(deck), card_pick(deck)]
    d_hand = [card_pick(deck), card_pick(deck)]
    print("The Dealer's: {}".format(d_hand[1:]))
    while True:
        dupdate = Hand.Hand.dealer_check(d_hand)
        print("Your hand: {}".format(p_hand))
        print("Your point total is: {}".format(Hand.Hand.hand_check(p_hand)))
        update = Hand.Hand.hand_check(p_hand)
        if update > 21:
            print("You lose!")
            break
        decision = input('Hit or Stay? ').lower()
        if decision == 'hit':
            p_hand.append(card_pick(deck))
        elif decision == 'stay':
            dup = dealer_protocol(d_hand, deck)
            print("The dealer is worth: {}".format(dup))
            duplex = Hand.Hand.dealer_check(dup)
            if update == duplex:
                print("TIE!")
                break
            elif update > duplex or duplex > 21:
                print('You WIN!')
                break
            else:
                print("You lose!")
                break

game()
while True:
    again = input("Would you like to play again? y/n: ")
    if again == 'y':
        game()
    else:
        print("You'll be back")
        exit()
            # Hand.check
            # initialize dealer, END()
