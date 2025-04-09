# Digit Factorial Chains
# The number 145 is well known for the property that 1! + 4! + 5! = 145
# Less well known is 169 in that it produces the longest chain of numbers that link back to 169; 
# it turns out that there are only three such loops that exist:
# 169 -> 363601 -> 1454 -> 169
# 871 -> 45361 -> 871 
# 872 -> 45362 -> 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example:
# 69 -> 363600 -> 1454 -> 169 -> 363601 -> 1454, therefore it is repeated
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million
# is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms
import math

factorial_cache = {i: math.factorial(i) for i in range(10)}

def digit_factorial(n):
    return sum(factorial_cache[int(digit)] for digit in str(n))

def chain_length(n, cache):
    seen = {}  
    current = n
    steps = 0
    
    while current not in seen:
        seen[current] = steps
        current = digit_factorial(current)
        steps += 1
        
        if current in cache:  # Use memoized value if available
            total_length = steps + cache[current]
            for num, index in seen.items():
                cache[num] = total_length - index  # Store length in cache
            return total_length

    # Loop detected, update cache
    loop_start = seen[current]
    loop_length = steps - loop_start

    for num, index in seen.items():
        if index >= loop_start:
            cache[num] = loop_length  # Numbers in loop store only loop size
        else:
            cache[num] = steps - index  # Numbers before loop store full chain length

    return steps

def count_sixty_term_chains(limit):
    """Count numbers below `limit` that produce exactly 60-term chains."""
    cache = {}  # Memoization cache
    count = 0
    
    for n in range(1, limit):
        if chain_length(n, cache) == 60:
            count += 1

    return count

# Find the count for numbers below 1,000,000
result = count_sixty_term_chains(1_000_000)
print("Number of chains with exactly 60 non-repeating terms:", result)



