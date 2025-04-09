#What is the 10001st prime number
#To solve we could try generate prime numbers in a list and then return index 10000
def kth_prime(k):
    list_of_primes = [2]
    n = 3
    while len(list_of_primes) < k:
        for p in list_of_primes:
            if n % p == 0:
                break         #if n % p == 0 then n isn't prime so can break
        else:      #if n % i != 0 in this range then prime so add to list of primes
            list_of_primes.append(n)
        n += 2
    return list_of_primes[-1]

print(kth_prime(10001))