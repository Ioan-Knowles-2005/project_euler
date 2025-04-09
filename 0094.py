# Almost Equilateral Triangles
# It is easily proved that no equilateral triangle exists with integer length sides and integer area.
# However 5-5-6 has area 12 
# We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed 1,000,000,000
import numpy as np
import math

#def exact_area(a, b, c):
 #   base = a
  #  height = np.sqrt(b**2 - (a**2 / 4))
   # area = 1/2 * base * height
    #return area

#def perimeter(a, b, c):
 #   return a + b + c

#def almost_equi(perimeter_limit):
 #   a, b, c, d = 1, a, a + 1, a - 1
  #  perimeter_total = 0
   # while perimeter(a, b, d) < perimeter_limit:
    #    if exact_area(a, b, c).is_integer():
     #       perimeter_total += a + b + c
      #  if exact_area(a, b, d).is_integer():
       #     perimeter_total += a + b + d
        #a, b, c, d += 1
    #return perimeter_total

#Will take too long

import math

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(math.isqrt(n))
    return r * r == n

def valid_case1(a):
    # For almost equilateral triangle with sides (a, a, a+1)
    # The condition for integer area is: 3a^2 - 2a - 1 = 4x^2 for some integer x.
    lhs = 3 * a * a - 2 * a - 1
    return (lhs >= 0 and lhs % 4 == 0 and is_perfect_square(lhs // 4))

def valid_case2(a):
    # For triangle with sides (a, a, a-1)
    # The condition is: 3a^2 + 2a - 1 = 4x^2 for some integer x.
    lhs = 3 * a * a + 2 * a - 1
    return (lhs >= 0 and lhs % 4 == 0 and is_perfect_square(lhs // 4))

def generate_case1(limit):
    """
    Generate all 'a' values for triangles of type (a, a, a+1)
    with perimeter P = 3a+1 <= limit.
    """
    a = 5
    while 3 * a + 1 <= limit:
        if valid_case1(a):
            yield a
        a += 1  # increment by 1 to find all solutions

def generate_case2(limit):
    """
    Generate all 'a' values for triangles of type (a, a, a-1)
    with perimeter P = 3a-1 <= limit.
    """
    a = 17
    while 3 * a - 1 <= limit:
        if valid_case2(a):
            yield a
        a += 1  # increment by 1

def solve_almost_equilateral(limit=10**9):
    total_perimeter = 0
    
    # Case 1: Triangles of form (a, a, a+1), perimeter = 3a+1
    for a in generate_case1(limit):
        P = 3 * a + 1
        total_perimeter += P
    
    # Case 2: Triangles of form (a, a, a-1), perimeter = 3a-1
    for a in generate_case2(limit):
        P = 3 * a - 1
        total_perimeter += P
    
    return total_perimeter

result = solve_almost_equilateral(10**9)
print("Sum of perimeters for all almost equilateral triangles <= 1e9:", result)
