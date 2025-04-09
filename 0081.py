# Path Sum: Two Ways
# Find the minimal path sum from the top left to the bottom right by only moving right and down in problem_81_matrix.txt

import numpy as np
import heapq

def load_matrix(filename):
    """Load the matrix from a file into a NumPy array."""
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.split(','))) for line in f]
    return np.array(matrix)

matrix = load_matrix("problem_81_matrix.txt")

def dijkstra_minimal_path_sum(matrix):
    """Finds the minimal path sum from top-left to bottom-right using Dijkstra's Algorithm."""
    rows, cols = len(matrix), len(matrix[0])
    directions = [(1, 0), (0, 1)]  # Move only right (0,1) and down (1,0)

    # Priority queue for Dijkstra (cost, row, col)
    pq = [(matrix[0][0], 0, 0)]  # Start from the top-left corner
    min_cost = np.full((rows, cols), float('inf'))  # Store minimal cost to reach each cell
    min_cost[0][0] = matrix[0][0]

    while pq:
        cost, r, c = heapq.heappop(pq)  # Get the least cost node

        # If we reached the bottom-right, return the cost
        if r == rows - 1 and c == cols - 1:
            return cost

        # Explore right and down neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:  # Stay within bounds
                new_cost = cost + matrix[nr][nc]
                if new_cost < min_cost[nr][nc]:  # Only update if we find a lower cost
                    min_cost[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

print(dijkstra_minimal_path_sum(matrix))