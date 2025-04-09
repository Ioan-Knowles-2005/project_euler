#Odd period square roots
#Exactly four continued fractions, for N <= 13, have an odd period.
#How many continued fractions for N <= 10000 have an odd period?
import math

def continued_fraction_period(n):
    """Returns the period of the continued fraction representation of sqrt(n)"""
    a0 = int(math.sqrt(n))
    if a0 * a0 == n:
        return 0  # Perfect square, so no period

    # Initialize values
    m, d, a = 0, 1, a0
    seen = {}

    period = 0
    while (m, d, a) not in seen:
        seen[(m, d, a)] = period
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1

    return period - seen[(m, d, a)]

# Count how many values of N (2 ≤ N ≤ 10,000) have an odd period
max_N = 10_000
odd_period_count = sum(1 for N in range(2, max_N + 1) if continued_fraction_period(N) % 2 == 1)
print("Number of continued fractions with an odd period for N ≤ 10,000:", odd_period_count)
