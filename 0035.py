# Circular Primes
# The number 197 is called a circular prime because all rotations of the number are also prime
# 197, 719, 971
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97
#How many circular primes are below 1 million
def is_prime(n):
    if n < 2:
        return False
    # Check divisibility up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#We now have a function to determine whether a number n is prime we will only have to check those numbers
def get_rotations(n):
    s = str(n)
    rotations = []
    for i in range(1, len(s)):
        rotated = s[-i:] + s[:-i]
        rotations.append(int(rotated))
    return rotations
#This function outputs a list of all the rotations of a number n
def is_circular_prime(n):
    if not is_prime(n):
        return False
    for rotation in get_rotations(n):
        if not is_prime(rotation):
            return False
    return True
#This function checks if a number is circularly prime
def number_of_circular_prime():
    total = 1     #start from 1 because we know 2 is circularly prime
    for i in range(1, 1000001, 2):
        if is_circular_prime(i):
            total += 1
    return total

print(number_of_circular_prime())



