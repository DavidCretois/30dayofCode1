import tkinter as tk
import colours as c
import random

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100, 0))

    def make_GUI(self):
        self.cells= []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i, colum=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, colum=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.apprend(cell_data)
            self.cells.apprend(row)

        score_frame = tk.Frame(self)
        score_frame.place(reLx=0.5, y=45, anchar="center")
        tk.Label(
            score_frame,
            text="Score",
            font=c.SCORE_LABEL_FONT
        ).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_FONT)
        self.score_label.grid(row=1)

    def start_game(self):

        self.matrix = [[0] * 4 for _ in range(4)]

        row = random.randint(0, 3)
        co1 = random.randint(0, 3)
        self.maxtrix[row][co1] = 2
        self.cells[row][co1]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][co1]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )
        while(self.matrix[row][co1] !=0):
            row = random.randint(0, 3)
            co1 = random.randint(0, 3)
        self.maxtrix[row][co1] = 2
        self.cells[row][co1]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][co1]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )

        self.score = 0

    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill.position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                 if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]
