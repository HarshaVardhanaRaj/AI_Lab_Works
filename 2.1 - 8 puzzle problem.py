from collections import deque

def get_neighbours(state):
    neighbours = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)

            new_state[zero_index], new_state[new_index] = (
                new_state[new_index],
                new_state[zero_index]
            )

            neighbours.append(tuple(new_state))

    return neighbours


def bfs(start, goal):
    queue = deque([tuple(start)])
    visited = {tuple(start): None}

    while queue:
        current = queue.popleft()

        if current == tuple(goal):
            path = []

            while current is not None:
                path.append(current)
                current = visited[current]

            return path[::-1]

        for neighbour in get_neighbours(current):
            if neighbour not in visited:
                visited[neighbour] = current
                queue.append(neighbour)

    return None


start = [
         1, 2, 3,
         4, 0, 6,
         7, 5, 8
        ]

goal = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
       ]

solution = bfs(start, goal)

if solution:
    print("Solution found!")
    print("No. of moves:", len(solution) - 1)
    print()

    step = 0
    for state in solution:
        print("Step", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
        step += 1
else:
    print("No solution found.")
