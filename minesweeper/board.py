"""
Name: Board.py
Function: board class for minesweeper game that displays the board
Inputs: None
Outputs: None
External sources: pygame documentation for reference 
Authors: Mo Osby, Drew Franke, Alex Lanter
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

        #on first click, place mines then reveal
        if self.game.first_click:
            self.game.place_mines(col, row)

        if self.game.game_over:
            return
        self.game.reveal_cell(col, row)

        if self.game.game_over:
            print("Game Over! You clicked on a mine.")
            

    #Import Assets
    def loadAssets(self):

        #Store all assets
        self.tiles = {}
        self.events = {}

        # List of event sprite names
        events = {"unknown" : "TileUnknown", 
                  "empty": "TileEmpty", 
                  "flag": "TileFlag", 
                  "mine": "TileMine", 
                  "explosion": "TileExploded"}
        #List of numbered tiles

        tile_range = range(1,9)

        # Load and resize numbered tiles
        for i in tile_range:
            self.tiles[i] = pygame.image.load(f"assets/Tile{i}.png").convert_alpha()
            self.tiles[i] = pygame.transform.scale(self.tiles[i], (self.tile_size, self.tile_size))

        # Load and resize event sprites
        for event, i in events.items():
            self.events[event] = pygame.image.load(f"assets/{i}.png").convert_alpha()
            self.events[event] = pygame.transform.scale(self.events[event], (self.tile_size, self.tile_size))



    def draw(self, screen):
        #Load in asset files
        self.loadAssets()

        #Draw board onto the screen
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.x + col * self.tile_size
                y = self.y + row * self.tile_size

                #Change tiles based on the event after click
                if self.game.game_over and (col, row) == self.game.exploded_mine:
                    event = self.events["explosion"]
                elif (col, row) in self.game.revealed:
                    event = self.events["empty"]
                elif self.game.game_over and (col, row) in self.game.mines:
                    event = self.events["mine"]
                else:
                    event = self.events["unknown"]

                screen.blit(event, (x,y))

                pygame.draw.rect(
                    screen,
                    "black",
                    (x, y, self.tile_size, self.tile_size), 2
                )

                #Draw number adjacent mines (unless=0)
                if (col, row) in self.game.revealed and (col, row) not in self.game.mines:
                    count = self.game.adjacent_mines.get((col, row), 0) #Get mine number
                    if count > 0:
                        text = self.font.render(str(count), True, "black") #Draw the number of mines to middle of tile
                        text_rect = text.get_rect(center=(x + self.tile_size // 2, y + self.tile_size // 2))
                        screen.blit(text, text_rect)
