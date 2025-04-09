#in the UK there are qight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
#It is possible to make £2 in the following way:
# (1* £1) + (1* 50p) + (2 * 20p) + (1 * 5p) + (1 * 2p) + (3 * 1p)
#How many different ways can £2 be made using any number of coin?
def two_pounds():
    list_of_coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    # Create a list to hold the number of ways to make each amount from 0 to target.
    # ways[i] will hold the number of ways to make i pence.
    ways = [0] * (target + 1)
    ways[0] = 1  # There's exactly one way to make 0p: use no coins
    # For each coin, update the ways array.
    for coin in list_of_coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    return ways[target]
print(two_pounds())
