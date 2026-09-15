"""
Name: Board.py
Function: board class for minesweeper game that displays the board
Inputs: None
Outputs: None
External sources: pygame documentation for reference 
Authors: Mo Osby, Drew Franke
Date: 09/12/2026
"""
import pygame
from minesweeper import Minesweeper
class Board:
    def __init__(self, rows, cols, num_mines=10):
        self.rows = rows
        self.cols = cols
        self.tile_size = 50

        self.x = 25
        self.y = 25
        self.game = Minesweeper(num_mines, rows, cols)  # Initialize the Minesweeper game with 10 mines


    def handle_click(self, mouse_x, mouse_y):
        #convert mouse click position to board coordinates
        col = (mouse_x - self.x) // self.tile_size
        row = (mouse_y - self.y) // self.tile_size

        #ignore clicks outside the board
        if col < 0 or col >= self.cols or row < 0 or row >= self.rows:
            return

        #on first click, place mines then reveal
        if self.game.first_click:
            self.game.place_mines(col, row)

        #don't reveal an already revealed cell
        if (col, row) not in self.game.revealed:
            self.game.reveal_cell(col, row)
        
        

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.x + col * self.tile_size
                y = self.y + row * self.tile_size

                if (col, row) in self.game.revealed:
                    color = "white"
                elif (col, row) in self.game.mines:
                    color = "red"
                else:
                    color = "gray"

                pygame.draw.rect(
                    screen,
                    color,
                    (x, y, self.tile_size, self.tile_size)
                )

                pygame.draw.rect(
                    screen,
                    "black",
                    (x, y, self.tile_size, self.tile_size), 2
                )
