"""
Name: main.py
Function: main function for minesweeper game that starts the game, displays some board details and detects player interaction.
Inputs: Number of mines, left and right mouse events
Outputs: Drawings rendered to pygame window, Win event, Loss event
External sources: pygame documentation for reference
Authors: Mo Osby, Drew Franke, Vrishank Kulkarni, Alex Lanter
Date Created: 09/12/2026
Date Last Edited: 09/20/2026
"""
import pygame 
from board import Board

pygame.init()
screen = pygame.display.set_mode((650, 650))
font = pygame.font.Font("assets/ThaleahFat.ttf", 32)
small_font = pygame.font.Font("assets/ThaleahFat.ttf", 16)

def draw_input_screen(user_input, error):
    screen.fill("white")

    title_text = font.render("Minesweeper", True, "black")
    screen.blit(title_text, (650 // 2 - title_text.get_width() // 2, 200))

    instructions_text = small_font.render("Select number of mines (10-20):", True, "black")
    screen.blit(instructions_text, (650 // 2 - instructions_text.get_width() // 2, 270))

    input_box = pygame.Rect(275, 320, 100, 40)
    pygame.draw.rect(screen, "lightgray", input_box)
    pygame.draw.rect(screen, "black", input_box, 2)
    typed = font.render(user_input, True, "black")
    screen.blit(typed, (input_box.x + 10, input_box.y + 10))

    hint = small_font.render("Press Enter to start", True, "gray")
    screen.blit(hint, (650 // 2 - hint.get_width() // 2, 380))

    if error:
        error_text = small_font.render(error, True, "red")
        screen.blit(error_text, (650 // 2 - error_text.get_width() // 2, 420))

    pygame.display.flip()

user_input = ""
error = ""
at_start = True

while at_start:
    draw_input_screen(user_input, error)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.isdigit() and 10 <= int(user_input) <= 20:
                    num_mines = int(user_input)
                    at_start = False
                else:
                    error = "Please enter a number between 10 and 20."
                    user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
                error = ""
            elif event.unicode.isdigit() and len(user_input) < 2:
                user_input += event.unicode
                error = ""
                


board = Board(10, 10, num_mines=num_mines)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.handle_click(*event.pos)

            elif event.button == 3:
                board.place_flag(*event.pos)

    screen.fill("white")
    board.draw(screen)

    # Change the status text for playing/lose/win
    if board.game.game_over:
        if board.game.won:
            status_text = font.render("Victory!", True, "green")
        else:
            status_text = font.render("Game Over!", True, "red")
    else:
        status_text = font.render("Playing", True, "black")
    #text placement
    screen.blit(status_text, (650 // 2 - status_text.get_width() // 2, 550))
    pygame.display.flip()
    
pygame.quit()
