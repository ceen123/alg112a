
#refrence 
#https://www.geeksforgeeks.org/python-program-for-rat-in-a-maze-backtracking-2/
#chat gpt


def safe(maze, x, y):
    return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and (maze[x][y] == 0 or maze[x][y] == 'C')

def dfs(maze, x, y, visited):
    if not safe(maze, x, y) or visited[x][y]:
        return False

    # Mark the current cell as visited
    visited[x][y] = True

    # If the mouse has reached the cheese
    if maze[x][y] == 'C':
        return True

   
    if safe(maze, x + 1, y) and dfs(maze, x + 1, y, visited):
        return True
    if safe(maze, x, y + 1) and dfs(maze, x, y + 1, visited):
        return True
    if safe(maze, x - 1, y) and dfs(maze, x - 1, y, visited):
        return True
    if safe(maze, x, y - 1) and dfs(maze, x, y - 1, visited):
        return True

    return False

def solve_maze(maze, start):
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    return dfs(maze, start[0], start[1], visited)

# 0 = open path, 1 = wall, 'C' = cheese
maze = [[0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 'C']]

# Starting position
start = (0, 0)

if solve_maze(maze, start):
    print("Path to the cheese found!")
else:
    print("No path to the cheese.")
