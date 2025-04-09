#Pandigital Prime
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
import itertools

def is_prime(n):
    if n < 2:
        return False
    # Check divisibility up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_pandigital_prime():
    max_prime = 0
    # Use 7-digit pandigital numbers since 8 and 9-digit ones are divisible by 3.
    digits = '7654321'
    for p in itertools.permutations(digits):
        num = int(''.join(p))
        if is_prime(num) and num > max_prime:
            max_prime = num
    return max_prime

print(largest_pandigital_prime())

