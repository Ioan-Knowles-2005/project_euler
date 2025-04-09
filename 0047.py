#Distinct Prime Factors
#The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 * 7, 15 = 3 * 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644, 645, 646
# Find the first four consecutive integers to have four distinct prime factors each. 
# What is the first of these numbers?
#
import sympy

def count_distinct_prime_factors(n):
    return len(set(sympy.primefactors(n)))


def find_consecutive_numbers_with_n_prime_factors(target_count, consecutive_count):
    num = 2
    consecutive_found = 0
    while True:
        if count_distinct_prime_factors(num) == target_count:
            consecutive_found += 1
            if consecutive_found == consecutive_count:
                return num - consecutive_count + 1  # Return the first number in the sequence
        else:
            consecutive_found = 0  # Reset count if sequence breaks

        num += 1
