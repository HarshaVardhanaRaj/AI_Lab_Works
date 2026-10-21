import math

# Total sticks at the start
TOTAL_STICKS = 15

# -----------------------------
# Minimax with Alpha-Beta Pruning
# -----------------------------
def minimax(sticks, is_ai_turn, alpha, beta):
    # No sticks left
    if sticks == 0:
        if is_ai_turn:
            return -1   # Human took the last stick
        else:
            return 1    # AI took the last stick

    if is_ai_turn:
        best = -math.inf

        for move in range(1, 4):
            if sticks >= move:
                score = minimax(sticks - move, False, alpha, beta)
                best = max(best, score)

                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = math.inf

        for move in range(1, 4):
            if sticks >= move:
                score = minimax(sticks - move, True, alpha, beta)
                best = min(best, score)

                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

# -----------------------------
# AI chooses best move
# -----------------------------
def ai_move(sticks):
    best_score = -math.inf
    best_move = 1

    for move in range(1, 4):
        if sticks >= move:
            score = minimax(sticks - move, False,
                            -math.inf, math.inf)

            if score > best_score:
                best_score = score
                best_move = move

    return best_move

# -----------------------------
# Main Game
# -----------------------------
sticks = TOTAL_STICKS

print("====== TAKE AWAY GAME ======")
print("Rules:")
print("- Remove 1, 2, or 3 sticks.")
print("- Whoever takes the LAST stick wins.\n")

while sticks > 0:

    print("\nSticks Remaining:", sticks)
    print("| " * sticks)

    # Human move
    while True:
        try:
            player = int(input("Your move (1-3): "))

            if player not in [1, 2, 3]:
                print("Choose 1, 2, or 3.")
                continue

            if player > sticks:
                print("Not enough sticks.")
                continue

            break

        except ValueError:
            print("Enter a valid number.")

    sticks -= player

    if sticks == 0:
        print("\nYou took the last stick.")
        print("You Win!")
        break

    # AI move
    move = ai_move(sticks)
    print("\nAI removes", move, "stick(s).")

    sticks -= move

    if sticks == 0:
        print("\nAI took the last stick.")
        print("AI Wins!")
        break
