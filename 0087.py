# Prime Power Triples
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

# 7071^2 = 50,000,000 so only need to generate primes up to 7071

def sieve(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

limit = 50_000_000
primes = sieve(7071)

squares = [p**2 for p in primes if p**2 < limit]
cubes   = [p**3 for p in primes if p**3 < limit]
fourths = [p**4 for p in primes if p**4 < limit]

numbers = set()

for s in squares:
    for c in cubes:
        if s + c >= limit:
            break  # Since c increases, no need to continue for this s.
        for f in fourths:
            total = s + c + f
            if total < limit:
                numbers.add(total)
            else:
                break

print(len(numbers))
