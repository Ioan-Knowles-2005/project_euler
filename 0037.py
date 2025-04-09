# Truncatable Primes
#The number 3797 has an interesting property 
#Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:  
#3797, 797, 97, 7
#Similarly we can work from right to left: 
#3797, 379, 37, 3

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
def is_prime(n):
    if n < 2:
        return False
    # Check divisibility up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_to_right_removal(n):
    str_n = str(n)
    list_of_left_right_numbers = []
    for i in range(len(str_n)):
        new_str = str_n[i:]
        list_of_left_right_numbers.append(int(new_str))
    return list_of_left_right_numbers

def right_to_left_removal(n):
    str_n = str(n)
    list_of_right_left_numbers = []
    for i in range(len(str_n)):
        new_str = str_n[:len(str_n)-i]
        list_of_right_left_numbers.append(int(new_str))
    return list_of_right_left_numbers

def is_truncatable_prime(n):
    if n < 10:
        return False
    for num in right_to_left_removal(n):
        if not is_prime(num):
            return False
    for num in left_to_right_removal(n):
        if not is_prime(num):
            return False
    return True
    
def sum_of_truncatable_primes():
    total = 0
    n = 11
    truncatable_primes = []
    while len(truncatable_primes) <= 10:
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
            total += n
        n += 2
    return total

print(sum_of_truncatable_primes())