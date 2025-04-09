# Prime Permutations
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 
# 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?
import sympy as sp
def is_permutation(a, b, c):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

def prime_permutations():
    primes = list(sp.primerange(1000, 10000))
    prime_set = set(primes)
    answer = []
    for prime in prime_set:
        for i in range(1000, 5000):
            if (prime + i) in prime_set and (prime + 2*i) in prime_set and is_permutation(prime, prime + i, prime + 2*i):
                answer.append(prime), answer.append(prime + i), answer.append(prime + 2 * i)
                break
    return str(answer[0]) + str(answer[1]) + str(answer[2])

print(prime_permutations())