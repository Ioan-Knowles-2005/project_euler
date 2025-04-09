# Spiral Primes
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is 
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed
# If this process is continued, what is the side length of the square spiral for which the ratio of primes
# along both diagonals first falls below 10%
# Let side length = s, TR = s^2 - 3*(s-1), TL = s^2 - 2 * (s-1), BL = s^2 - (s-1), BR = s^2,

def is_prime(n):
    if n < 2:
        return False
    # Check divisibility up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def spiral_primes():
    list_of_diagonals = [False, True, True, True, False]
    s = 5
    while sum(list_of_diagonals) / len(list_of_diagonals) > 0.1:
        top_right = int(s**2 - 3*(s-1))
        top_left = int(s**2 - 2*(s-1))
        bottom_left = int(s**2 - (s-1))
        bottom_right = int(s**2)
        diagonals_given_s = [top_right, top_left, bottom_left, bottom_right]
        for position in diagonals_given_s:
            if is_prime(position):
                list_of_diagonals.append(True)
            else:
                list_of_diagonals.append(False)
        if s % 1001 == 0:
            print(f"The side length is {s} and the diagonal values are {top_right, top_left, bottom_left, bottom_right}.")
        s += 2
    return s - 2

print(spiral_primes())
    

        

