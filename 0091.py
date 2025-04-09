# Right angled triangles with integer coordinates
# The points P(x1, y1) and Q(x2, y2) are plotted at integer coordinates and form a triangle with the origin OPQ
# There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between
# 0 and 2 that is inclusive 0 <= x1, x2, y1, y2 <= 2
# Given that 0<= x1, x2, y1, y2 <= 50. How many right angled triangles can be formed

import math

def count_right_triangles(grid_size):
    # Right angles at the origin
    at_origin = grid_size * grid_size

    # Right angles at (x1, y1)
    at_p = int(1/ 100 * sum(x + y for x in range(1, grid_size + 1) for y in range(1, grid_size + 1)))

    # Right triangles with hypotenuse aligned with the grid
    at_hypotenuse = sum(math.gcd(x, y) for x in range(1, grid_size + 1) for y in range(1, grid_size + 1))

    return at_origin + 2 * at_p + at_hypotenuse

print(count_right_triangles(50))