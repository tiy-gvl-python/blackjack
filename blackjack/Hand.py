import re


class Hand():

    def hand_check(hand):
        points = 0
        for card in hand:
            if 'jack' in card or 'queen' in card or 'king' in card or 'ten' in card:
                points += 10
            elif 'ace' in card:
                ace = input('Ace high? or low? ')
                if ace == 'high':
                    points += 11
                if ace == 'low':
                    points += 1
            elif re.match(r'\d*', card) is not None:
                points += int(re.match(r'\d', card).group())
        return points

    def dealer_check(hand):
        points = 0
        for card in hand:
            if 'jack' in card or 'queen' in card or 'king' in card or 'ten' in card:
                points += 10
            elif 'ace' in card:
                    points += 11
            elif re.match(r'\d*', card) is not None:
                points += int(re.match(r'\d', card).group())
        return points
