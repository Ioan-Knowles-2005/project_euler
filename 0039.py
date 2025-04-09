#Integer right triangles
#If p is the perimeter of a right angle triangle with integral length sides, (a, b, c), there are
#  exactly three solutions for p = 120
#{20,48,52}, {24, 45, 51}, {30, 40, 50}
import numpy as np

def total_solutions(): 
    max_number_of_solutions = 0
    max_perimeter = None
    for p in range(1, 1001):
        solutions = []
        for a in range(1, p//3 + 1):
            for b in range(a, (p - a) // 2 + 1):
                c_val = np.sqrt(a**2 + b**2)
                if c_val.is_integer():
                    c = int(c_val)
                    if b < c and (a + b + c) == p:
                        solutions.append((a, b, c))
        if len(solutions) > max_number_of_solutions:
            max_perimeter = p
            max_number_of_solutions = len(solutions)
    return max_perimeter

print(total_solutions())  
    
