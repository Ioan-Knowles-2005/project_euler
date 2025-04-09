# Large Non-Mersenne Prime
# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
# 2^(6972593) - 1; it contains exactly 2098960 digits
# Subsequently other Mersenne primes, of the form 2^p - 1, have been found which contain more digits.
# However, in 2004 there was found a massive non-Mersenne prime which contains 2357207 digits:
# 28433 * 2^7830457 + 1
#Find the last 10 digits of this prime number
def large_non_mersenne_prime():
    mod = 10**10
    power = pow(2, 7830457, mod)
    return (28433 * power + 1) % mod

print(large_non_mersenne_prime())
