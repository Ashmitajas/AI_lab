from pyamaze import maze, agent, textLabel
from collections import deque

# ---------------- DFS ----------------
def DFS(m):
    start = (m.rows, m.cols)
    stack = [start]
    visited = [start]
    dfsPath = {}

    while stack:
        cell = stack.pop()
        if cell == (1, 1):
            break

        for d in 'ESNW':
            if m.maze_map[cell][d]:
                if d == 'E':
                    nextCell = (cell[0], cell[1] + 1)
                elif d == 'W':
                    nextCell = (cell[0], cell[1] - 1)
                elif d == 'N':
                    nextCell = (cell[0] - 1, cell[1])
                elif d == 'S':
                    nextCell = (cell[0] + 1, cell[1])

                if nextCell not in visited:
                    visited.append(nextCell)
                    stack.append(nextCell)
                    dfsPath[nextCell] = cell

    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    return fwdPath


# ---------------- BFS ----------------
def BFS(m):
    start = (m.rows, m.cols)
    queue = deque([start])
    visited = [start]
    bfsPath = {}

    while queue:
        cell = queue.popleft()
        if cell == (1, 1):
            break

        for d in 'ESNW':
            if m.maze_map[cell][d]:
                if d == 'E':
                    nextCell = (cell[0], cell[1] + 1)
                elif d == 'W':
                    nextCell = (cell[0], cell[1] - 1)
                elif d == 'N':
                    nextCell = (cell[0] - 1, cell[1])
                elif d == 'S':
                    nextCell = (cell[0] + 1, cell[1])

                if nextCell not in visited:
                    visited.append(nextCell)
                    queue.append(nextCell)
                    bfsPath[nextCell] = cell

    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]

    return fwdPath


# ---------------- Main ----------------
m = maze(6, 6)          # 👈 change size to play (e.g., 10x10)
m.CreateMaze()

dfsPath = DFS(m)
bfsPath = BFS(m)

# Agents
a1 = agent(m, footprints=True, filled=True, color='red')
a2 = agent(m, footprints=True, color='blue')

# Trace paths
m.tracePath({a1: dfsPath})
m.tracePath({a2: bfsPath})

# Labels
textLabel(m, 'DFS Path', len(dfsPath) + 1)
textLabel(m, 'BFS Path', len(bfsPath) + 1)

m.run()
