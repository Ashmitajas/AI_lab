from pyamaze import maze, agent, textLabel

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


# -------- Main --------
m = maze(10,10)
m.CreateMaze()

path = DFS(m)

a = agent(m, footprints=True, filled=True, color='red')
m.tracePath({a: path})

textLabel(m, 'DFS Path Length', len(path) + 1)
m.run()
