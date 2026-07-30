import heapq
def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def a_star(grid,start,goal):
    rows,cols = len(grid),len(grid[0])
    open_list = []
    heapq.heappush(open_list,(heuristic(start,goal),0,start,[start]))
    visited = set()
    while open_list:
        f,g,current,path = heapq.heappop(open_list)
        if current == goal:
            return path
        if current in visited :
            continue
        visited.add(current)
        x,y = current
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if (0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0):
                next_node = (nx,ny)
                heapq.heappush(open_list,(g+1 + heuristic (next_node,goal),g+1,next_node,path+[next_node]))
    return None
grid = [
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
    ]
start = (0,0)
goal = (4,4)
path = a_star(grid,start,goal)
print("Path found:\n",path)
