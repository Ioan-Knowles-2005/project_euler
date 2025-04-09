# Totient Permutation
# The number 1 is is considered to be relatively prime to every positive number, so phi(1) = 1
# phi(87109) = 79180 and it can be seen that 79180 is a permutation of 87109
# Find the value of n, 1 < n < 10**7, for which phi(n) is a permutation of n and the ratio n / phi(n) produces a minimum
import math
import itertools
from collections import Counter

def totient_function(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count

def is_permutation(n):
    return Counter(str(n)) == Counter(str(totient_function(n)))

def totient_perm():
    minimum_sum = float('inf')
    n_minimum_sum = 0
    for n in range(3, 10**7, 2):
        if is_permutation(n):
            print(f"phi({n}) = {totient_function(n)}")
            if (n / totient_function(n)) < minimum_sum:
                minimum_sum = n / totient_function(n)
                n_minimum_sum = n
    return n_minimum_sum

#print(totient_perm())
#This will take ages to run this is a faster way from chatgpt
from math import isqrt
from collections import defaultdict

def compute_totient_sieve(limit):
    """Precompute Euler's Totient function for all numbers up to 'limit'."""
    phi = list(range(limit + 1))  # Initialize phi(n) = n
    
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, limit + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i  # Apply the formula phi(n) = n * (1 - 1/p)
    
    return phi

def is_permutation(a, b):
    """Check if two numbers are permutations of each other."""
    return sorted(str(a)) == sorted(str(b))

def find_min_totient_perm(limit):
    """Find n ≤ limit for which n/phi(n) is minimized, and phi(n) is a permutation of n."""
    phi = compute_totient_sieve(limit)

    min_ratio = float('inf')
    best_n = 0

    for n in range(2, limit):
        if is_permutation(n, phi[n]):  # Check if n and phi(n) are permutations
            ratio = n / phi[n]
            if ratio < min_ratio:
                min_ratio = ratio
                best_n = n

    return best_n

# Find the result for n ≤ 10^7
result = find_min_totient_perm(10**7)

print(f"The value of n ≤ 10^7 that minimizes n/φ(n) and is a permutation is: {result}")


    
