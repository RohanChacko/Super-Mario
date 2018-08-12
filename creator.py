import numpy as np
from colorama import *
from collision import CheckCollision
from generator import live_pillars, pillar_top, pillar_side
init()

grid = np.zeros(shape=(80, 93), dtype=str)
initial_x=0
initial_y=63
cur_x = initial_x
cur_y = initial_y

mario_grid = ["    ▄████▄▄", "   ▄▀█▀▐└─┐", "  █▄▐▌▄█▄┘", "   └▄▄▄▄─┘",
              "▄███▒██▒███▄", "▒▒█▄▒▒▒▒▄█▒▒", "  ▒▒▒▀▀▒▒▒", "▄███    ███▄"]

################################################################################

def jumper(cur_x, cur_y):
    pass

def mario_create(column, row):
    """
        Creates Mario at a particular coordinate
    """

    temp1 = column
    for r in range(8):
        column = temp1
        if row < 80:
            for pixel in range(len(mario_grid[r])):
                grid[row][column] = mario_grid[r][pixel]
                #print(row, column)
                column = column + 1
            row = row + 1

def pillar_print(column, row, times):

    temp1 = column
    row = row - times - 1

    for r in range(11   ):
        grid[row][column] = pillar_top[0][r]
        column = column + 1
    column = temp1
    row = row + 1

    for r in range(times):
        column = temp1
        for pixel in range(len(pillar_side[0])):
            grid[row][column] = pillar_side[0][pixel]
            column = column + 1
        row = row + 1


# Colouring ground: green sky:blue

# -1: move left
# +1: move right
#  0:don't move
# +2:jump
def grid_bg(pos_symbol):
    """
        Creates the complete grid with all objects in it
    """
    global cur_x
    global cur_y
    pil = 0
    if pos_symbol == 1:
        cur_x = cur_x + 5

    elif pos_symbol == -1:
        cur_x = cur_x - 5

    elif pos_symbol == 2:
        jumper(cur_x,cur_y)

    else:
        pass

    cur_x, cur_y = CheckCollision(cur_x,cur_y, pos_symbol)

    #RESET GRID
    for row in range(np.size(grid, 0)):

        for column in range(np.size(grid, 1)):
            grid[row][column]="0"

    #MANIPULATE GRID
    for row in range(np.size(grid, 0)):

        for column in range(np.size(grid, 1)):

            if row == cur_y and column == cur_x:
                mario_create(cur_x, cur_y)
            if row == 70 and pil <len(live_pillars) and column == live_pillars[pil][0]:
               pillar_print(column, row, live_pillars[pil][1])
               pil = pil + 1


    for row in range(np.size(grid, 0)):

        for column in range(np.size(grid, 1)):
            if grid[row][column] != "0":
                print(grid[row][column],end='')
            elif grid[row][column] == "0" and row <=70:
                print(' ',end='')
            if row > 70:
                print("#",end='')
        print('')
