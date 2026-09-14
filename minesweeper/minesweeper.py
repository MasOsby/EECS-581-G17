"""
Name: minesweeper.py
Function: class to hold the logic for minesweeper game
Inputs: None
Outputs: None
External sources: None
Authors: Drew Franke, Mo Osby
date: 09/13/2026
"""
import random

class Minesweeper:
    def __init__(self, num_mines, rows, cols):
        self.num_mines = num_mines
        self.mines = set()
        self.revealed = set()
        self.first_click = True
        self.rows = rows
        self.cols = cols


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

    def reveal_cell(self, col, row):
        if (col, row) not in self.revealed:
            self.revealed.add((col, row))
        # Check for if user clicks on a mine 
        if (col, row) in self.mines:
            self.revealed.add((col, row))  # Reveal the mine cell    
            return False  # Game over
        return True  # Continue game
