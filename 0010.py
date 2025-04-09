#Find the sum of all primes below 2 million(limit)
#Generate primes then add to sum
def sum_of_primes(limit):
    sieve = [True]*limit    #list of booleans where the indices represents that number
    sieve[0] = sieve[1] = [False]   #0 and 1 aren't primes therefore mark as false
    for i in range(2, int(limit**0.5)+1):   #iterate from 2,3,4,5,6,...,1000001
        if sieve[i]:                       #if a number i is prime, mark all multiples as not prime
            for j in range(i*i, limit, i):
                sieve[j]=False
    return sum(idx for idx, is_prime in enumerate(sieve) if is_prime)
    #if is_prime = True then sum index
    #returning sum of all indices where still True


print(sum_of_primes(2000000))