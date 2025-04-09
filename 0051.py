#Find the smallest prime which, by replacing part of the number with the same digit
#is part of an eight prime value family

#56003 is an example of a 7 prime value family as:
#56003, 56113, 56333, 56443, 56663, 56773, 56993 are all prime and that is 7/10

#Note: Doesn't have to be adjacent digits and could be more than 2 digits replaced 
# We know that 56003 is the smallest 7 prime value family so no need to check lower than that
#First we will assume it is two digits replaced and find smallest instance
#Going to have at least one repeated digit

import itertools

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n*0.5), 2):
        if n % i == 0:
            return False
    return True
#This function simply checks if a number n is prime

def get_family(prime_str, indices):
    """
    Given a prime number (as a string) and a tuple of indices (positions) in that string,
    this function replaces the digits at those positions with each digit from '0' to '9'
    and returns a list of candidate numbers (as integers) that are prime.
    """
    family = []
    for digit in '0123456789':
        if indices[0] == 0 and digit == '0': #This is to avoid leading zeroes for example 13 is a 6 prime value family
            continue                         #[13,23,43,53,73,83] not 7 as 03 doesn't count
        candidate = list(prime_str)
        for index in indices:
            candidate[index] = digit   #This replaces the indices with the digits
        # Convert the modified list back to an integer.
        candidate_num = int("".join(candidate))
        # If the candidate number is prime, add it to the family.
        if is_prime(candidate_num):
            family.append(candidate_num)
    return family

def find_smallest_prime_eight_family():
    n = 56003
    while True:
        if is_prime(n):
            prime_str = str(n)
            for digit in set(prime_str):
                # Get all positions (indices) where this digit occurs in the string
                positions = [i for i, d in enumerate(prime_str) if d == digit]
                # Generate all non-empty combinations of these positions.
                # For example, if the digit appears twice, try replacing just the first, just the second,
                # and then both.
                for r in range(1, len(positions) + 1):
                    for indices in itertools.combinations(positions, r):
                        # Get the family by replacing the digits at the chosen indices.
                        family = get_family(prime_str, indices)
                        # Check if the family has at least 8 prime members.
                        if len(family) >= 8:
                            # Optionally, you can print the family for verification:
                            # print("Family found for", n, "with replacement indices", indices, ":", family)
                            return n
        # Only check odd numbers; even numbers (except 2) cannot be prime.
        n += 2

result = find_smallest_prime_eight_family()
print(result)