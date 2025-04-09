# Ordered Fractions
# Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n, d) = 1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8  in ascending order of size, It can be seen that 2/5 is the fraction immediately to the 
# left of 3/7 
# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to 
# the left of 3/7

# 3/7 ~ 0.4285714286

import math

def find_left_fraction(limit):
    target_n, target_d = 3, 7
    best_n, best_d = 0, 1

    for d in range(1, limit + 1):
        n = (target_n * d - 1) // target_d
        if math.gcd(n, d) == 1:  
            if n * best_d > best_n * d: 
                best_n, best_d = n, d
                print(best_n/best_d)

    return best_n

print(find_left_fraction(1000000))


