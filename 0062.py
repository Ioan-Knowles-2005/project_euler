# Cubic Permutations
# The cube, 41063625 (345^3) can be permuted to produce two other cubes, 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cubes.
# Find the smallest cube for which exactly five permutations of its digits are cube.

from collections import defaultdict

def find_smallest_cube():
    cubes = defaultdict(list)  # Dictionary to store cubes by their sorted digit signature
    n = 345
    
    while True:
        cube = n ** 3
        key = "".join(sorted(str(cube)))  
        cubes[key].append(cube)

        if len(cubes[key]) >= 3:
            print(cubes[key])

        if len(cubes[key]) == 5:
            return min(cubes[key])  
        
        n += 1

print(find_smallest_cube())


