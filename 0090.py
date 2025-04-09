# Cube-Digit Pairs
import itertools

def can_form_all_squares(cube1, cube2, squares):
    """
    Checks if the two cubes (each a set of digits) can form all required 2-digit squares.
    A square (x, y) can be formed if x is on one cube and y on the other, or vice versa.
    """
    for (x, y) in squares:
        # Must be able to place x on one cube, y on the other, in either order.
        if not ((x in cube1 and y in cube2) or (y in cube1 and x in cube2)):
            return False
    return True

def solve_cube_digit_pairs():
    # Define the squares in "merged 6/9" form:
    # e.g. '09' => (0,6), '16' => (1,6), '49' => (4,6), etc.
    squares = [(0,1), (0,4), (0,6),  # 01, 04, 09
               (1,6), (2,5), (3,6),  # 16, 25, 36
               (4,6), (6,4), (8,1)]  # 49, 64, 81

    # We'll treat digits as from 0..8, where "6" also covers "9".
    digits = range(9)  # 0,1,2,3,4,5,6,7,8

    # Generate all 6-digit combinations from these 9 merged digits.
    # Each combination is a possible labeling of one cube.
    combos = list(itertools.combinations(digits, 6))

    count = 0
    seen_pairs = set()

    # Check all pairs (comboA, comboB) with comboA <= comboB to avoid double-counting.
    for i, comboA in enumerate(combos):
        cubeA = set(comboA)
        for comboB in combos[i:]:
            cubeB = set(comboB)
            # Build a canonical representation so that swapping cubes doesn't double-count.
            # We can store them as sorted tuples.
            pair_key = tuple(sorted([tuple(sorted(cubeA)), tuple(sorted(cubeB))]))
            if pair_key in seen_pairs:
                continue

            # Check if these two cubes can form all squares
            if can_form_all_squares(cubeA, cubeB, squares):
                count += 1
            seen_pairs.add(pair_key)

    return count

result = solve_cube_digit_pairs()
print("Number of distinct cube arrangements allowing all squares to be formed:", result)


