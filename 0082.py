# Path Sum: Three Ways
#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing
# in any cell in the right column, and only moving up, down, and right, is indicated by "x"; 
# the sum is equal to 994
# ( 131 ,  673, "234", "103",  "18")
# ("201",  "96","342",  965 ,  150 )
# ( 630 ,  803,  746 ,  422 ,  111 )
# ( 537 ,  699,  497 ,  121 ,  956 )
# ( 805 ,  732,  524 ,   37 ,  331 )
#Find the minimal path sum from the left column to the right column in matrix.txt containing an 80x80 matrix

import numpy as np
import heapq

def load_matrix(filename):
    """Load the matrix from a file into a NumPy array."""
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.split(','))) for line in f]
    return np.array(matrix)

def dijkstra_min_path(matrix):
    """Find the minimal path sum from the left column to the right column using Dijkstra’s algorithm."""
    rows, cols = matrix.shape
    # Priority queue for Dijkstra's algorithm (cost, row, col)
    pq = []
    # Distance matrix to store minimum path sum to reach each cell
    dist = np.full((rows, cols), np.inf)

    # Initialize priority queue with all leftmost column values
    for r in range(rows):
        heapq.heappush(pq, (matrix[r, 0], r, 0))
        dist[r, 0] = matrix[r, 0]

    # Possible movements: right (0,1), down (1,0), up (-1,0)
    directions = [(0, 1), (1, 0), (-1, 0)]

    while pq:
        current_sum, r, c = heapq.heappop(pq)

        # Stop if we reached the rightmost column
        if c == cols - 1:
            return current_sum

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols:
                new_sum = current_sum + matrix[new_r, new_c]

                if new_sum < dist[new_r, new_c]:
                    dist[new_r, new_c] = new_sum
                    heapq.heappush(pq, (new_sum, new_r, new_c))

    return np.min(dist[:, -1])  # The minimum value in the rightmost column

# Load the 80x80 matrix
matrix = load_matrix("problem_82_matrix.txt")

# Compute and print the minimal path sum
min_path_sum = dijkstra_min_path(matrix)
print("Minimal path sum from left to right column:", min_path_sum)
