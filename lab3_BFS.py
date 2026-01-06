from pyamaze import maze, agent, textLabel
from collections import deque

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


# -------- Main --------
m = maze(30,40)
m.CreateMaze()

path = BFS(m)

a = agent(m, footprints=True, filled=True, color='blue')
m.tracePath({a: path})

textLabel(m, 'BFS Path Length', len(path) + 1)
m.run()
