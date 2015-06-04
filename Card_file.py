class Card:
    def count(self, hand, person):
        self.counter = 0
        for card in hand:
            if card[0] == 'A' or card[1] == 'A' and person == "player":
                self.to_do = input("11 or 1 ")
                if self.to_do == '11':
                    self.counter += 11
                else:
                    self.counter += 1
            elif card[0] == 'A' or card[1] == 'A':
                self.counter += 11
            else:
                if card[0].isupper():
                    self.counter += 10
                if card[1].isupper():
                    self.counter += 10
                if card[0].isdigit():
                    self.counter += int(card[0])
                if card[1].isdigit():
                    self.counter += int(card[1])
        # print("Your count is ", self.counter)
        if self.counter == 21 and person == "player":
            print("blackjack")
            exit()
        elif self.counter > 21 and person == "player":
            print("Lose")
            exit()
        elif self.counter == 21 and person == "dealer":
            print("Dealer Wins because of blackjack")
            exit()
        elif self.counter > 21 and person == "dealer":
            print("You Win dealer busted at ", self.counter)
            exit()

        # add together check if they go over 21 or equal 21
