# Arithmetic Expressions
# By using each of the digits from the set, {1, 2, 3, 4} exactly once, and making use of the four arithmetic operations (+,-,*,/}
# and brackets/parentheses, it is possible to form different positive integer targets. For example:
# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1/2)
# 19 = 4 * (2 + 3) - 1
# 36 = 4 * 3 * (2 + 1)
# Using the set {1, 2, 3, 4} there is 31 different target numbers and 36 is the largest and each of the numbers 1 to 28  can be obtained before
# encountering the first non-expressible number.
# Find the set of four distinct digits, a < b < c < d for which the longest set of consecutive positive integers, 1 to n  can be obtained,
# giving your answer as a string: abcd.

import math
from itertools import permutations, combinations, product

def all_expressions_results(digits):
    """
    Given a 4-tuple of digits (e.g., (1,2,3,4)), generate all possible
    values obtainable by inserting +, -, *, / and parentheses in every way.

    Returns a set of floating-point results (we'll interpret them as real numbers).
    """
    # A helper to perform safe division (avoid dividing by zero).
    def safe_div(x, y):
        if abs(y) < 1e-12:
            return None
        return x / y

    # We'll define all possible binary operations as functions:
    def op_plus(x, y):
        return x + y
    def op_minus(x, y):
        return x - y
    def op_times(x, y):
        return x * y
    def op_div(x, y):
        return safe_div(x, y)

    operations = [op_plus, op_minus, op_times, op_div]

    results = set()

    # We consider the 5 ways to parenthesize 4 numbers (Catalan structure):
    # 1) ((a op b) op c) op d
    # 2) (a op (b op c)) op d
    # 3) (a op b) op (c op d)
    # 4) a op ((b op c) op d)
    # 5) a op (b op (c op d))

    a, b, c, d = digits

    # We'll define a small helper that tries to combine x and y with an operation:
    # returns None if invalid (like division by zero).
    def try_ops(x, y):
        """Generate all possible results of x (op) y for the 4 ops, ignoring None."""
        out = []
        for op in operations:
            val = op(x, y)
            if val is not None:
                out.append(val)
        return out

    # We systematically compute:

    # 1) ((a op b) op c) op d
    for x in try_ops(a, b):
        for y in try_ops(x, c):
            for z in try_ops(y, d):
                results.add(z)

    # 2) (a op (b op c)) op d
    for x in try_ops(b, c):
        for y in try_ops(a, x):
            for z in try_ops(y, d):
                results.add(z)

    # 3) (a op b) op (c op d)
    for x in try_ops(a, b):
        for y in try_ops(c, d):
            for z in try_ops(x, y):
                results.add(z)

    # 4) a op ((b op c) op d)
    for x in try_ops(b, c):
        for y in try_ops(x, d):
            for z in try_ops(a, y):
                results.add(z)

    # 5) a op (b op (c op d))
    for x in try_ops(c, d):
        for y in try_ops(b, x):
            for z in try_ops(a, y):
                results.add(z)

    return results

def consecutive_run_length(values):
    """
    Given a set of positive integer values, find how many consecutive
    integers starting at 1 are present. For example, if values has {1,2,3,4,5,7},
    the run length is 5 because 6 is missing.
    """
    length = 0
    n = 1
    while n in values:
        length += 1
        n += 1
    return length

def solve_arithmetic_expressions():
    best_length = 0
    best_digits = None

    # We only pick from digits 1..9 (distinct). 0 is excluded in Project Euler #93 context.
    for combo in combinations(range(1, 10), 4):
        # For each 4-digit combination, we gather all possible results (using permutations).
        # Then collect which positive integers appear.
        possible_ints = set()

        for perm in permutations(combo):
            # Evaluate all possible expressions from these 4 digits in order.
            results = all_expressions_results(perm)
            # For each result, if it's positive and "almost integer," add int(...) to set.
            for val in results:
                # We'll interpret it as integer if it's within floating tolerance.
                if val > 0:
                    # Round to nearest integer
                    rounded = round(val)
                    if abs(val - rounded) < 1e-7:
                        possible_ints.add(rounded)

        # Now measure how many consecutive integers from 1 up appear in possible_ints
        run_len = consecutive_run_length(possible_ints)
        if run_len > best_length:
            best_length = run_len
            best_digits = combo

    # Format the best digits as a string "abcd"
    return "".join(str(d) for d in best_digits)

def main():
    answer = solve_arithmetic_expressions()
    print("The set of digits yielding the longest consecutive run is:", answer)

if __name__ == "__main__":
    main()
