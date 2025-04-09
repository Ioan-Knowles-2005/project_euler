# Prime Pair Sets
# The primes 3, 7, 109 and 673 are quite remarkable By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109 both 7109 and 1097 are prime
# The sume of these four primes 792 represents the lowest sum for a set of four primes with this property
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from itertools import combinations
from sympy import isprime

def sieve(limit):
    """Generate a list of primes using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def are_concatenations_prime(p1, p2):
    """Check if both concatenations of p1 and p2 are prime."""
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))

def find_prime_pair_set(prime_list, set_size=5):
    """Find the lowest sum set of 'set_size' primes where any two concatenate to a prime."""
    prime_pairs = {}

    # Precompute valid prime pairs
    for p1, p2 in combinations(prime_list, 2):
        if are_concatenations_prime(p1, p2):
            prime_pairs.setdefault(p1, []).append(p2)
            prime_pairs.setdefault(p2, []).append(p1)

    # Backtracking search to find valid prime sets
    def search(prime_set):
        if len(prime_set) == set_size:
            return prime_set  # Found valid set

        # Try adding another prime that maintains the property
        for candidate in prime_pairs.get(prime_set[-1], []):
            if candidate > prime_set[0] and all(candidate in prime_pairs[p] for p in prime_set):
                result = search(prime_set + [candidate])
                if result:
                    return result

        return None

    # Iterate over primes and attempt to build valid sets
    for p in prime_list:
        result = search([p])
        if result:
            return result

    return None

# Generate primes up to a reasonable limit
primes = sieve(10000)

# Find the prime set and compute the lowest sum
prime_set = find_prime_pair_set(primes, set_size=5)
lowest_sum = sum(prime_set) if prime_set else None

print("Lowest sum of five primes forming a valid set:", lowest_sum)
print("Prime set:", prime_set)
