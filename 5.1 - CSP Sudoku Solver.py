def solve_sudoku(puzzle):

    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:

                # Try numbers 1 to 9
                for num in range(1, 10):

                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num

                        # Recursively solve
                        if solve_sudoku(puzzle):
                            return True

                        # Backtrack
                        puzzle[row][col] = 0

                return False

    return True


def is_valid(puzzle, row, col, num):

    # Check row
    for i in range(9):
        if puzzle[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if puzzle[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False

    return True


# 0 represents an empty cell
puzzle = [
         [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],

         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],

         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

if solve_sudoku(puzzle):
    for row in puzzle:
        print(row)
else:
    print("No solution")
