def attack(board, row, col):
    n = len(board)

    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return True  # Attacked

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return True
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return True
        i -= 1
        j += 1

    return False


def solve_n_queens(n=8):
    def backtrack(row=0):
        if row == n:
            results.append([r[:] for r in board])  # Deep copy
            return

        for col in range(n):
            if not attack(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0  # Backtrack

    board = [[0] * n for _ in range(n)]
    results = []

    backtrack()

    return results


solutions = solve_n_queens()

print(f"Total solutions: {len(solutions)}\n")
print("First valid solution as 0/1 matrix:")

for row in solutions[0]:
    print(row)
