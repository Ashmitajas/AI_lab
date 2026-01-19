import tkinter as tk
import random
import heapq
from tkinter import messagebox

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

class EightPuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Game")
        self.root.resizable(False, False)

        self.tiles = []
        self.buttons = []
        self.moves = 0

        self.create_widgets()
        self.shuffle_board()

    # ---------- UI ----------
    def create_widgets(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame, font=("Arial", 20, "bold"),
                width=4, height=2,
                command=lambda i=i: self.move_tile(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        self.status = tk.Label(self.root, text="Moves: 0", font=("Arial", 12))
        self.status.pack(pady=5)

        tk.Button(self.root, text="Hint (Shortest Path)",
                  command=self.give_hint).pack(pady=3)

        tk.Button(self.root, text="New Game",
                  command=self.shuffle_board).pack(pady=3)

    # ---------- GAME ----------
    def shuffle_board(self):
        nums = list(range(9))
        while True:
            random.shuffle(nums)
            if self.is_solvable(nums) and tuple(nums) != GOAL:
                break
        self.tiles = nums
        self.moves = 0
        self.update_ui()

    def update_ui(self):
        for i, val in enumerate(self.tiles):
            if val == 0:
                self.buttons[i].config(text="", state="disabled", bg="lightgray")
            else:
                self.buttons[i].config(text=str(val), state="normal")
        self.status.config(text=f"Moves: {self.moves}")

    def move_tile(self, index):
        z = self.tiles.index(0)
        if self.is_adjacent(index, z):
            self.tiles[z], self.tiles[index] = self.tiles[index], self.tiles[z]
            self.moves += 1
            self.update_ui()

            if tuple(self.tiles) == GOAL:
                messagebox.showinfo("Solved 🎉",
                                    f"Solved in {self.moves} moves!")

    def is_adjacent(self, i, j):
        r1, c1 = divmod(i, 3)
        r2, c2 = divmod(j, 3)
        return abs(r1 - r2) + abs(c1 - c2) == 1

    def is_solvable(self, board):
        inv = 0
        nums = [x for x in board if x != 0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    inv += 1
        return inv % 2 == 0

    # ---------- A* HINT SYSTEM ----------
    def give_hint(self):
        path = self.a_star(tuple(self.tiles))
        if path and len(path) > 1:
            self.tiles = list(path[1])  # apply ONE optimal move
            self.moves += 1
            self.update_ui()
        else:
            messagebox.showinfo("Hint", "Already solved!")

    def a_star(self, start):
        pq = []
        heapq.heappush(pq, (0, start))
        came_from = {start: None}
        g_score = {start: 0}

        while pq:
            _, current = heapq.heappop(pq)

            if current == GOAL:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative = g_score[current] + 1
                if neighbor not in g_score or tentative < g_score[neighbor]:
                    g_score[neighbor] = tentative
                    f = tentative + self.manhattan(neighbor)
                    heapq.heappush(pq, (f, neighbor))
                    came_from[neighbor] = current
        return None

    def reconstruct_path(self, came_from, current):
        path = [current]
        while came_from[current]:
            current = came_from[current]
            path.append(current)
        return path[::-1]

    def get_neighbors(self, state):
        neighbors = []
        z = state.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                neighbors.append(tuple(new))
        return neighbors

    def manhattan(self, state):
        dist = 0
        for i, val in enumerate(state):
            if val == 0:
                continue
            goal_i = GOAL.index(val)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_i, 3)
            dist += abs(r1 - r2) + abs(c1 - c2)
        return dist


if __name__ == "__main__":
    root = tk.Tk()
    EightPuzzleGUI(root)
    root.mainloop()