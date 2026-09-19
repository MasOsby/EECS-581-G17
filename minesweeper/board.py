"""
Name: Board.py
Function: board class for minesweeper game that displays the board
Inputs: None
Outputs: None
External sources: pygame documentation for reference 
Authors: Mo Osby, Drew Franke, Alex Lanter, Vrishank Kulkarni 
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
        self.font = pygame.font.Font(None, 32)  # font for drawing adjacent-mine numbers

    def handle_click(self, mouse_x, mouse_y):
        #convert mouse click position to board coordinates
        col = (mouse_x - self.x) // self.tile_size
        row = (mouse_y - self.y) // self.tile_size

        #ignore clicks outside the board
        if col < 0 or col >= self.cols or row < 0 or row >= self.rows:
            return

        # do not reveal a cell that has a flag
        if (col, row) in self.game.flags:
            return

        #on first click, place mines then reveal
        if self.game.first_click:
            self.game.place_mines(col, row)

        #Don't need to check for if cell already revealed because reveal_cell now handles it (recursive base case)
        safe=self.game.reveal_cell(col, row)

        if not safe:
            print("Game Over! You clicked on a mine.")
            #text = self.font.render("Game Over", True, "black")
            #text_rect =  text.get_rect()

            #"TODO: Implement all mines revealed and game over screen"



    def place_flag(self, mouse_x, mouse_y):
        # convert mouse click position to board coordinates
        col = (mouse_x - self.x) // self.tile_size
        row = (mouse_y - self.y) // self.tile_size

        # ignore clicks outside the board
        if col < 0 or col >= self.cols or row < 0 or row >= self.rows:
            return

        cell = (col, row)

        # do not place flags on revealed cells
        if cell in self.game.revealed:
            return

        # if the cell already has a flag, remove it
        if cell in self.game.flags:
            self.game.flags.remove(cell)

        # otherwise, place a flag if there are flags available
        elif len(self.game.flags) < self.game.num_mines:
            self.game.flags.add(cell)

        
        

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

                
                # draw a flag if the cell is flagged
                if (col, row) in self.game.flags:
                    flag_text = self.font.render("F", True, "red")

                    flag_rect = flag_text.get_rect(
                        center=(
                            x + self.tile_size // 2,
                            y + self.tile_size // 2
                        )
                    )

                    screen.blit(flag_text, flag_rect)

                #Draw number adjacent mines (unless=0)
                if (col, row) in self.game.revealed and (col, row) not in self.game.mines:
                    count = self.game.adjacent_mines.get((col, row), 0) #Get mine number
                    if count > 0:
                        text = self.font.render(str(count), True, "black") #Draw the number of mines to middle of tile
                        text_rect = text.get_rect(center=(x + self.tile_size // 2, y + self.tile_size // 2))
                        screen.blit(text, text_rect)
