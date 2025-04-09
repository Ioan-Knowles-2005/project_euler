#Goldbach's Other conjecture
# It was proposed by Christian Goldbach that every odd composite number (number that it isn't prime)
#  can be written as the sum of a prime and twice a square.
# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
#It turn out that the conjecture was false
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math

def is_odd_composite(n):
    if n < 9 or n % 2 == 0 or is_prime(n):
        return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_odd_composite():
    i = 9
    while True:
        if is_odd_composite(i):
            valid = False
            for p in range(2, i):
                if is_prime(p):
                    k_squared = (i - p) / 2
                    if k_squared.is_integer() and math.isqrt(int(k_squared))**2 == k_squared:
                        valid = True
                        break
            if not valid:
                return i
        i += 2
    return i

print(first_odd_composite())
                            

