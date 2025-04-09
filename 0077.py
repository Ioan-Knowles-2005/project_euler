# Prime Summations
# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def count_prime_partitions(n, primes):
    dp = [0] * (n + 1)
    dp[0] = 1  # one way to make sum 0
    for p in primes:
        for x in range(p, n + 1):
            dp[x] += dp[x - p]
    return dp[n]

def find_first_over(limit):
    n = 2
    while True:
        # Get primes up to n (n is small; this is efficient for our search)
        primes = sieve(n)
        partitions = count_prime_partitions(n, primes)
        if partitions < limit:
            print(f"{n} has under {limit} prime partitions, it only has {partitions}")
        if partitions > limit:
            return n, partitions
        n += 1

# We need the first value for which the number of ways exceeds 5000
target_limit = 5000
result, ways = find_first_over(target_limit)
print("The first value which can be written as the sum of primes in over 5000 different ways is:", result)
print("Number of ways:", ways)


