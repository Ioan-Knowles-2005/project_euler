# Diophantine Equation
# Consider quadratic Diophantine equations of the form: x^2 - D*y^2 = 1
# For example when D = 13 the minimal solution in x is 649^2 - 13 * 180^2 = 1
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7} we obtain the following:
# 3^2 - 2 * 2^2 = 1
# 2^2 - 3 * 1^2 = 1
# 9^2 - 5 * 4^2 = 1
# 5^2 - 6 * 2^2 = 1
# 8^2 - 7 * 3^2 = 1
# Hence by considering the minimal solutions in x for D <= 7, the largest x is obtained when D=5
# Find the value of D <= 1000 in minimal solutions in x for which the largest value of x is obtained

from math import isqrt

def continued_fraction_sqrt(D):
    """Compute the continued fraction representation of sqrt(D)."""
    m, d, a0 = 0, 1, isqrt(D)
    if a0 * a0 == D:
        return []  # D is a perfect square, no solution

    a = a0
    terms = [a0]
    
    while a != 2 * a0:  # Period detection
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        terms.append(a)
    
    return terms

def solve_pell(D):
    """Finds the minimal solution for x in x^2 - D*y^2 = 1."""
    terms = continued_fraction_sqrt(D)
    if not terms:
        return None  # No solution

    a0 = terms[0]
    period = terms[1:]

    # Compute convergents to find the minimal solution
    p, q = [a0, a0 * period[0] + 1], [1, period[0]]

    for i in range(2, 2 * len(period)):  # Double the period to ensure correctness
        a_n = period[(i - 1) % len(period)]
        p.append(a_n * p[-1] + p[-2])
        q.append(a_n * q[-1] + q[-2])
        if p[-1] ** 2 - D * q[-1] ** 2 == 1:
            return p[-1]  # Minimal x found

def find_largest_x(limit):
    """Find the value of D <= limit that produces the largest minimal x."""
    max_x, best_D = 0, 0

    for D in range(2, limit + 1):
        if isqrt(D) ** 2 == D:
            continue  # Skip perfect squares
        
        x = solve_pell(D)
        if x and x > max_x:
            max_x, best_D = x, D

    return best_D

# Find D for which the largest x is obtained
result = find_largest_x(1000)
print("The value of D ≤ 1000 for which the largest minimal x is obtained:", result)
