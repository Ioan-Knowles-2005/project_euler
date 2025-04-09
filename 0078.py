# Coin Partitions
#Let p(n) represent the number of different ways in which n coins can be separated into piles.
#  For example, five coins can be separated into piles in exactly seven different ways, so:
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which  p(n) is divisible by one million.

def find_least_partition_divisible_by(mod):
    # p[0] is defined as 1.
    partitions = [1]
    n = 1
    while True:
        p = 0
        k = 1
        # Use the generalized pentagonal numbers: k(3k−1)/2 and k(3k+1)/2.
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > n:
                break
            # sign alternates according to (-1)^(k-1)
            sign = (-1)**(k - 1)
            p += sign * partitions[n - g1]
            if g2 <= n:
                p += sign * partitions[n - g2]
            k += 1
        # Take modulo to prevent large integers
        p %= mod
        partitions.append(p)
        # Check if the partition number is divisible by mod
        if p == 0:
            return n
        n += 1


print(find_least_partition_divisible_by(10**6))

