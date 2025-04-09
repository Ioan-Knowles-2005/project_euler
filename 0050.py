#Consecutive Prime Sum
#41 can be written as the sum of six consecutive primes
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953

#Which prime, below one-million, can be written as the sum of the most consecutive primes?
import sympy as sp

def consecutive_prime_sum(limit):
    primes = list(sp.primerange(1, limit))
    prime_set = set(primes)

    max_length = 0
    max_prime = 0

    for start in range(len(primes)):
        for end in range(start + max_length, len(primes)):
            prime_sum = sum(primes[start:end])
            if prime_sum >= limit:
                break
            if prime_sum in prime_set:
                max_length = end - start
                max_prime = prime_sum
    return max_prime

print(consecutive_prime_sum(1000000))

