"""
Name: minesweeper.py
Function: class to hold the logic for minesweeper game
Inputs: None
Outputs: None
External sources: None
Authors: Drew Franke, Alex Lanter, Mo
date: 09/13/2026
"""
import random
class Minesweeper:
    def __init__(self, num_mines, rows, cols):
        self.num_mines = num_mines
        self.mines = set()
        self.revealed = set()
        self.flags = set()
        self.first_click = True
        self.rows = rows
        self.cols = cols
        self.adjacent_mines = {} #Dictionary to track adjacent mines per cell
        self.game_over = False  # Track if the game is over
        self.won = False  # Track if the player has won
        self.exploded_mine = None 


    def place_mines(self, safe_col, safe_row):
        #place mines randomly on the board, ensuring that the first clicked cell and its neighbors (3x3) are safe
        safe_cell = set()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                x, y = safe_col + i, safe_row + j
                if 0 <= x < self.cols and 0 <= y < self.rows:
                    safe_cell.add((x, y))

        all_cells = [(x, y) for x in range(self.cols) for y in range(self.rows) if (x, y) not in safe_cell]
        self.mines = set(random.sample(all_cells, self.num_mines))
        self.first_click = False
        self.calculate_adjacent()

    def calculate_adjacent(self):
        for col in range(self.cols):
            for row in range(self.rows):
                if (col, row) in self.mines: #Look at every cell, if it's a mine skip
                    continue

                count = 0 #start count at 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0: #Look at 3x3 around cell, skip cell itself
                            continue
                        x, y = col + i, row + j #grid space calculated from center plus offset in the 3x3
                        if 0 <= x < self.cols and 0 <= y < self.rows and (x, y) in self.mines: #if space inbounds and there's a mine increase count
                            count += 1

                self.adjacent_mines[(col, row)] = count #add found count to dictionary

    def reveal_cell(self, col, row):
        if (col, row) in self.flags:
            return True
        if (col, row) in self.revealed: 
            return True
        if (col, row) in self.mines:
            # self.revealed.add((col, row))  # Reveal the mine cell 
            self.exploded_mine = ((col, row))
            self.game_over = True  # Set game over flag   
            return False  # Game over
        if (col, row) not in self.revealed:
            self.revealed.add((col, row))
        if self.adjacent_mines.get((col, row), 0) == 0: #Get number of adjacent mines for space, keep going if it's 0
            for i in [-1, 0, 1]: 
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0: #Check 3x3 grid around cell, skip cell itself
                        continue
                    x, y = col + i, row + j #Get current cell inside 3x3 area being checked
                    if 0 <= x < self.cols and 0 <= y < self.rows: #If space is inbounds
                        self.reveal_cell(x, y) #Reveal it (which won't work if it's a mine or already revealed)
        #Win logic if the # of cells remaining is equal to num on mines
        safe_cells = (self.rows * self.cols) - self.num_mines
        if len(self.revealed) == safe_cells:
            self.game_over = True
            self.won = True
        return True
