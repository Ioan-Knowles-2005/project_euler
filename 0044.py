#Pentagonal Numbers
#Pn = n*(3n-1)/2
#It can be seen that P4 + P7 = P8 but their difference is not pentagonal
#Find the pair of pentagonal numbers Pi, Pj where their sum and difference is pentagonal and, 
# D = |Pi-Pj| is minimised; what is the value of D
import math

import math

def pentagonal_number(n):
    return n * (3*n - 1) // 2

def is_pentagonal(x):
    if x < 1: 
        return False
    # solve n from x = n(3n-1)/2 => 3n² - n - 2x = 0
    n = (1 + math.sqrt(1+24*x)) / 6
    return n.is_integer()

def find_min_pentagonal_diff():
    pentagonals = []
    pent_set = set()
    i = 1
    
    while True:
        pi = pentagonal_number(i)
        pentagonals.append(pi)
        pent_set.add(pi)
        
        # Check all pentagonal numbers that came before pi
        for pj in pentagonals[:-1]:
            diff = abs(pi - pj)
            summation = pi + pj
            if diff in pent_set and summation in pent_set:
                return diff  # first time we find it => smallest
                
        i += 1

print(find_min_pentagonal_diff())



    