#Triangular, Pentagonal, Hexagonal
#Triangular Tn = n(n+1)/2
#Pentagonal Pn = n(3n-1)/2
#Hexagonal Hn = n(2n-1)
#T285 = P165 = H143 = 40755
#Find the next triangle number which is also Pentagonal and Hexagonal
import math

def is_pentagonal(x):
    if x < 1: 
        return False
    n = (1 + math.sqrt(1+24*x)) / 6
    return n.is_integer()

def is_hexagonal(x):
    if x < 1:
        return False
    n = (1 + math.sqrt(1 + 8*x)) / 4
    return n.is_integer()

def generate_triangle(): #we will start from n = 286 
    n = 286
    result = 0
    while result == 0:
        triangle_formula = n*(n+1)/2
        if  is_hexagonal(triangle_formula) and is_pentagonal(triangle_formula):
            result = n
        n += 1
    return result * (result + 1) // 2

print(generate_triangle())

