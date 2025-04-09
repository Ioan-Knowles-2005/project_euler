# Path Sum: Four Ways
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is equal to 2297
# Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in problem_82_matrix.txt

import numpy as np
import heapq

def load_matrix(filename):
    """Load the matrix from a file into a NumPy array."""
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.split(','))) for line in f]
    return np.array(matrix)

matrix = load_matrix("problem_81_matrix.txt")

def dijkstra(matrix):
    """Uses Dijkstra's algorithm to find the minimal path sum in a matrix where moves are allowed in four directions."""
    rows, cols = len(matrix), len(matrix[0])
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue: (current_path_sum, row, col)
    pq = [(matrix[0][0], 0, 0)]
    
    # Create a 2D array to keep track of the minimal cost to reach each cell.
    best = [[float('inf')] * cols for _ in range(rows)]
    best[0][0] = matrix[0][0]
    
    while pq:
        cost, i, j = heapq.heappop(pq)
        
        # If we reached the bottom right, return the cost.
        if i == rows - 1 and j == cols - 1:
            return cost
        
        # If we already have a better cost for (i,j), skip this one.
        if cost > best[i][j]:
            continue
        
        # Check all four adjacent moves.
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                new_cost = cost + matrix[ni][nj]
                if new_cost < best[ni][nj]:
                    best[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
    
    # Return the best cost for bottom-right cell.
    return best[rows - 1][cols - 1]

print(dijkstra(matrix))