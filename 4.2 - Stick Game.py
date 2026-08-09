import math

def minimax(sticks, maximizing, alpha, beta):
    if sticks == 0:
        return -1 if maximizing else 1

    if maximizing:
        best = -math.inf

        for i in range(1, min(3, sticks) + 1):
            score = minimax(sticks - i, False, alpha, beta)
            best = max(best, score)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(1, min(3, sticks) + 1):
            score = minimax(sticks - i, True, alpha, beta)
            best = min(best, score)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


def best_move(sticks):
    best_score = -math.inf
    move = 1

    for i in range(1, min(3, sticks) + 1):
        score = minimax(sticks - i, False, -math.inf, math.inf)

        if score > best_score:
            best_score = score
            move = i

    return move


sticks = 10

print("STICK GAME")
print("There are 10 sticks.")
print("You can take 1, 2 or 3 sticks.")
print("Whoever takes the last stick wins!\n")

while sticks > 0:

    print("Sticks remaining:", sticks)

    # Player
    while True:
        player = int(input("Take 1, 2 or 3 sticks: "))

        if 1 <= player <= min(3, sticks):
            break

        print("Invalid move!")

    sticks -= player

    if sticks == 0:
        print("You took the last stick!")
        print("You WIN!")
        break

    # Computer
    computer = best_move(sticks)
    print("Computer takes:", computer)

    sticks -= computer

    if sticks == 0:
        print("Computer took the last stick!")
        print("Computer WINS!")
        break

    print()