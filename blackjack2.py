import random
import os


# This class is being used only to create a shuffled deck to draw from
class Deck:
    card_deck = [['A of clubs', 'A'], ['K of clubs', 10], ['Q of clubs',10], ['J of clubs',10],
                     ['10 of clubs',10], ['9 of clubs',9], ['8 of clubs',8], ['7 of clubs', 7],
                     ['6 of clubs',6], ['5 of clubs', 5], ['4 of clubs', 4], ['3 of clubs',3],
                     ['2 of clubs',2], ['A of hearts','A'], ['K of hearts', 10], ['Q of hearts', 10],
                     ['J of hearts',10], ['10 of hearts',10], ['9 of hearts', 9], ['8 of hearts', 8],
                     ['7 of hearts', 7], ['6 of hearts', 6], ['5 of hearts', 5], ['4 f hearts', 4],
                     ['3 of hearts', 3], ['2 of hearts', 2], ['A of diamonds','A'], ['K of diamonds', 10],
                     ['Q of diamonds', 10], ['J of diamonds', 10], ['10 of diamonds', 10],
                     ['9 of diamonds', 9], ['8 of diamonds', 8], ['7 of diamonds', 7],
                     ['6 of diamonds', 6], ['5 of diamonds', 5], ['4 of diamonds', 4],
                     ['3 of diamonds', 3], ['2 of diamonds', 2], ['A of spades','A'], ['K of spades', 10],
                     ['Q of spades', 10], ['J of spades', 10], ['10 of spades', 10], ['9 of spades', 9],
                     ['8 of spades', 8], ['7 of spades', 7], ['6 of spades', 6], ['5 of spades', 5],
                     ['4 of spades', 4], ['3 of spades', 3], ['2 of spades', 2]]


# this obviously is the generic hand used to create the players hands
class Hand:
     def __init__(self, name):
         self.name = name
         self.value_hand = []
         self.display_hand = []
     def initial_has_21(self):
         if "A" in self.value_hand and 10 in self.value_hand:
             return True
         else:
             return False
#class Dealer:

def initial_deal(deck, player_hand, dealer_hand):
    for i in range(2):
        live_card, card_value = deck.card_deck.pop()
        print(live_card)
        #return live_card
        player_hand.display_hand.append(live_card)
        player_hand.value_hand.append(card_value)
        live_card, card_value = deck.card_deck.pop()
        dealer_hand.display_hand.append(live_card)
        dealer_hand.value_hand.append(card_value)
    player_hand.value_hand = ["A", 10]
    if player_hand.initial_has_21() or dealer_hand.initial_has_21():
        print("Black Jack")
    print(player_hand.display_hand)
    print(player_hand.value_hand)
    print(dealer_hand.display_hand)
    print(dealer_hand.value_hand)

player_hand = Hand("Player 1")
dealer_hand = Hand("Dealer")
deck = Deck()
player_hand.value_hand = ["A", 10]
dealer_hand.value_hand = ["A", 9]

#initial_deal(deck, player_hand, dealer_hand)
#print(deck.card_deck)
#game = Dealer()
#game.init_hand(self, dealer_hand, player_hand, card)

#print('player display {}'.format(player_hand.display_hand))
#print('player value {}'.format(player_hand.value_hand))

#print('dealer display {}'.format(dealer_hand.display_hand))
#print('dealer value {}'.format(dealer_hand.value_hand))

#deal = Deal()
#deal.deal_init_hands()
