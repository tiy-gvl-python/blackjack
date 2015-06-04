# The player will start the game with $100.  Each play will cost $10

money = 100
cost = 10


def bankroll(money, cost):
    if money >= 10:
        money -+ cost
        print(money)
        return True
    else:
        return

bankroll(money, cost)
