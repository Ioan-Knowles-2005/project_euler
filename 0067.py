# Max Path Sum 2

def max_path_sum(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update each element by adding the max of adjacent numbers below
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

    return triangle[0][0]