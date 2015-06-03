class Card:
    def count(self, hand):
        self.count = 0
        for card in hand:
            # print(card)
            # print(card[0])
            # print(card[1])
            if card[0].isupper():
                self.count += 10
                if card[0] == 'A':
                    self.to_do = input("11 or 1 ")
                    if self.to_do == '11':
                        self.count += 11
                    else:
                        self.count += 1
            if card[1].isupper():
                self.count += 10
                if card[1] == 'A':
                    self.to_do = input("11 or 1 ")
                    if self.to_do == '11':
                        self.count += 11
                    else:
                        self.count += 1
            if card[0].isdigit():
                self.count += int(card[0])
            if card[1].isdigit():
                self.count += int(card[1])
        print("Your count is ", self.count)
        if self.count == 21:
            return "blackjack"
        elif self.count > 21:
            return "lose"
        else:
            pass

        # add together check if they go over 21 or equal 21
