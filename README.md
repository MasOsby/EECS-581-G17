# EECS-581 Group 17 Project 1
A 10x10 version of the classic puzzle game Minesweeper.

## Setup Instructions
1. Ensure Python version 3.13 is installed.

2. Clone the github repository

3. `cd` into `EECS-581-G17`

   You should see the folder `minesweeper` if you run `ls` (or `dir` on Windows)

4. Create the virtual environment by running:

   `python3.13 -m venv .venv`

5. Change environment to the virtual environment by running:

   If on Linux or MacOS: `source .venv/bin/activate`

   If on Windows: `source \.venv\Scripts\activate`

6. Install the pip package `pygame` by running: `pip install pygame`

   You should now see `pygame` in the installed package list if you run `pip list`

7. `cd` into the `minesweeper` folder

8. Finally, start the program by running the command: `python main.py`

## Controls

When you start up the game, you first have to enter the number of mines you want (10-20).

Then, use left click to uncover spaces and right click to toggle flags. Right click again to remove flags that have been placed. 

## System Architecture Documentation
[Link to page](minesweeper/docs/SystemArchitecture.md)
