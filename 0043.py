#Sub-String Divisibility
#The number 1406357289 is 0 to 9 pandigital, and has interesting sub-string divisibility property
#Let d1 be the 1st digit and d2 be the 2nd digit and so on
#d2d3d4 = 406 which is divisible by 2
#d3d4d5 = 063 which is divisible by 3
#d4d5d6 = 635 which is divisible by 5
#d5d6d7 = 357 which is divisible by 7
#d6d7d8 = 572 which is divisible by 11
#d7d8d9 = 728 which is divisible by 13
#d8d9d10 = 289 which is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.
import itertools

def list_of_pandigitals():
    digits = '0123456789'
    list_of_pandigital_numbers = []
    for perm in itertools.permutations(digits):
        if perm[0] == '0':
            continue
        pandigital_str = ''.join(perm)
        list_of_pandigital_numbers.append(int(pandigital_str))
    return list_of_pandigital_numbers

def prime_property(n):
    n_str = str(n)
    prime = [2, 3, 5, 7, 11, 13, 17]
    for i in range(2, 9):
        three_digits = int(n_str[i-1:i+2])
        if three_digits % prime[i-2] != 0:
            return False
    return True

def sum_of_prime_property():
    total = 0
    for pandigital in list_of_pandigitals():
        if prime_property(pandigital):
            total += pandigital
    return total

print(sum_of_prime_property())
