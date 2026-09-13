"""
Name: Board.py
Function: board class for minesweeper game that displays the board
Inputs: None
Outputs: None
External sources: pygame documentation for reference 
Authors: Mo Osby
Date: 09/12/2026
"""
import pygame
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tile_size = 50

        self.x = 25
        self.y = 25

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.x + col * self.tile_size
                y = self.y + row * self.tile_size

                pygame.draw.rect(
                    screen,
                    "grey",
                    (x, y, self.tile_size, self.tile_size)
                )

                pygame.draw.rect(
                    screen,
                    "black",
                    (x, y, self.tile_size, self.tile_size), 2
                )