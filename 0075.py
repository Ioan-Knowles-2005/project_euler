# Singular Integer Right Triangles
# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way,
# but there are many more examples:
# 12 (3, 4, 5)
# 24 (6, 8, 10)
# 30 (5, 12, 13)
# 36 (9, 12, 15) etc
# In contrast, some lengths of wire, like 20, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 it is possible to form exactly three different integer sided right angle triangles.
# Given that L  is the length of the wire, for how many values of l <= 1,500,000 can exactly one integer sided right angle triangle be formed?

#A primitive Pythagorean triple can be computed by:
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# when m > n > 0, gcd(m, n) = 1, m - n is odd
# perimeter = (m^2 - n^2) + 2mn + (m^2 + n^2) = 2m(m + n)

import math

def solve_pythagorean_perimeters(limit=1500000):
    # Array to count how many distinct right-angled triangles have perimeter p
    counts = [0] * (limit + 1)
    
    # Generate all primitive triples
    max_m = int(math.isqrt(750_000)) + 1 
    for m in range(2, max_m + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                p_primitive = 2 * m * (m + n)
                if p_primitive > limit:
                    break 
                multiple = p_primitive
                while multiple <= limit:
                    counts[multiple] += 1
                    multiple += p_primitive
    
    # Count how many perimeters have exactly one triple
    answer = sum(1 for p in range(1, limit + 1) if counts[p] == 1)
    return answer

result = solve_pythagorean_perimeters(1500000)
print(result)
