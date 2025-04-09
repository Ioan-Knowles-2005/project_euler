#Largest prime factor of 600851475143
def largest_prime_factor(n):
    factor = 2
    while n % 2 == 0:
        n //= 2   #floor division to return an int rather than a float

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2
    
    return n #if n > 1 then n itself is prime

print(largest_prime_factor(600851475143))