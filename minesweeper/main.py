"""
Name: main.py
Function: main function for minesweeper game that displays the board
Inputs: None
Outputs: None
External sources: pygame documentation for reference
Authors: Mo Osby
date: 09/12/2026
"""
import pygame 
from board import Board

pygame.init()
screen = pygame.display.set_mode((650, 650))

board = Board(10, 10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    board.draw(screen)
    pygame.display.flip()
pygame.quit()