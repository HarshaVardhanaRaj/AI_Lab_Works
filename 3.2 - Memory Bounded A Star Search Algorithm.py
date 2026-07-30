import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def memory_bounded_a_star(grid, start, goal, max_nodes):
    rows, cols = len(grid), len(grid[0])

    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), 0, start, [start]))

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        x, y = current

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == 0):

                next_node = (nx, ny)

                if next_node not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(next_node, goal)
                    new_path = path + [next_node]

                    heapq.heappush(open_list,
                                   (new_f, new_g, next_node, new_path))

                    # Memory limit check
                    if len(open_list) > max_nodes:
                        # Remove the node with the highest f-value
                        open_list.sort()
                        removed = open_list.pop()
                        heapq.heapify(open_list)

                        print("Memory limit reached. Removed node:",removed[2], "with f(n) =", removed[0])

    return None


# Grid (0 = free cell, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
max_nodes = 10

path = memory_bounded_a_star(grid, start, goal, max_nodes)

if path:
    print("\nPath found:")
    print(path)
else:
    print("\nNo path found.")
