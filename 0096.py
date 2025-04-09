# Su Doku
# Solve Sudoku files 
def read_sudoku_file(filename):
    """
    Reads sudoku puzzles from the given file.
    The file contains lines starting with "Grid XX" followed by 9 lines of digits.
    Returns a list of 9x9 grids (each grid is a list of lists of integers).
    """
    puzzles = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    i = 0
    while i < len(lines):
        if lines[i].startswith("Grid"):
            grid = []
            # Next 9 lines are the grid
            for j in range(i+1, i+10):
                # Convert each character to int
                grid.append([int(ch) for ch in lines[j].strip()])
            puzzles.append(grid)
            i += 10
        else:
            i += 1
    return puzzles

def is_valid(grid, row, col, num):
    """
    Check whether it's valid to assign 'num' to grid[row][col].
    It must not appear in the given row, column, or 3x3 subgrid.
    """
    # Check row
    if any(grid[row][c] == num for c in range(9)):
        return False
    # Check column
    if any(grid[r][col] == num for r in range(9)):
        return False
    # Check 3x3 subgrid:
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if grid[start_row + r][start_col + c] == num:
                return False
    return True

def solve_sudoku(grid):
    """
    Solves the sudoku puzzle using recursive backtracking.
    Returns True if a solution is found; the grid is modified in-place.
    """
    # Find the first empty cell (denoted by 0)
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # backtrack
                return False  # no valid number found, trigger backtracking
    return True  # no empty cell found, puzzle solved

def main():
    filename = "problem_96_sudoku.txt"  # Path to the file with sudoku puzzles
    puzzles = read_sudoku_file(filename)
    total_sum = 0
    
    for index, puzzle in enumerate(puzzles, start=1):
        if solve_sudoku(puzzle):
            # The top-left 3-digit number comes from the first row, columns 0, 1, and 2.
            # For example, if the first row is [4, 8, 3, ...], then the number is 483.
            top_left_number = int("".join(str(puzzle[0][i]) for i in range(3)))
            total_sum += top_left_number
        else:
            print(f"Puzzle {index} could not be solved.")
    
    print("The sum of the 3-digit numbers in the top left corner of each solved grid is:", total_sum)

if __name__ == "__main__":
    main()
