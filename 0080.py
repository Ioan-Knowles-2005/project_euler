# Square Root Digital Expansion
# It is well known that if the square root of a natural number is not an integer, then it is irrational.
# The decimal expansion of such square roots is infinite without any repeating pattern at all.
# The square root of two is 1.41421356237309504880 and the digital sum of the first one hundred decimal digits is 475
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the 
# irrational square roots.

import math
import decimal

decimal.getcontext().prec = 110

def is_perfect_square(n):
    root = int(math.isqrt(n))
    return root * root == n

def digital_sum_of_sqrt(n):
    sqrt_n = decimal.Decimal(n).sqrt()
    s = format(sqrt_n, 'f')
    s = s.replace('.', '')
    digits = s[:100]
    return sum(int(digit) for digit in digits)

def total_digital_sums(limit=100):
    total = 0
    for n in range(1, limit + 1):
        if not is_perfect_square(n):  
            total += digital_sum_of_sqrt(n)
    return total

result = total_digital_sums(100)
print("Total of the digital sums:", result)
