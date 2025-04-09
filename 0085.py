# Counting Rectangles
# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

# An m x n grid contains m*(m+1)*n*(n+1)/4 rectangles
# Therefore we can set a max dimension of 200 

def counting_rectangles(target, max_dimension):
    dimension = (0, 0)
    min_diff = float('inf')
    best_area = None
    for m in range(1, max_dimension + 1):
        for n in range(m, max_dimension + 1):
            rectangles = m * (m + 1) * (n) * (n + 1) / 4
            difference = abs(rectangles - target)
            if difference < min_diff:
                min_diff = difference
                best_area = m * n
                dimension = (m, n)
                if difference % 10 == 0:
                    print(difference)
    return f"Best area = {best_area}, dimension = {dimension} and the difference is {min_diff}"

print(counting_rectangles(2000000, 200))