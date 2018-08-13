import numpy as np
import time
from colorama import *
from collision import CheckCollision
from generator import live_pillars, pillar_top, pillar_side, cloud_1, cloud_2, live_cloud
init()

grid = np.zeros(shape=(80, 93), dtype=str)
initial_x = 0
initial_y = 67
cur_x = initial_x
cur_y = initial_y

mario_grid = [":::::", ":::::", ":::::", ":::::"]


################################################################################

def grid_print():
    global cur_x
    global cur_y

    # RESET GRID
    for row in range(np.size(grid, 0)):

        for column in range(np.size(grid, 1)):
            grid[row][column] = "0"

    # MANIPULATE GRID
    mario_create(cur_x, cur_y)
    for pil in range(len(live_pillars)):            #Put this line in the function pillar_print
        pillar_print(live_pillars[pil][0], 70, live_pillars[pil][1])

    for cloud in range(len(live_cloud)):
        cloud_print(live_cloud[cloud][0],live_cloud[cloud][1])

    for row in range(np.size(grid, 0)):

        for column in range(np.size(grid, 1)):
            if grid[row][column] != "0":
                print(grid[row][column], end='')
            elif grid[row][column] == "0" and row <= 70:
                print(' ', end='')
            if row > 70:
                print("#", end='')
        print('')


def jumper(jump_move):
    global cur_x
    global cur_y
    if jump_move == 0 :

        while cur_y > initial_y - 12:
            cur_y = cur_y - 3
            grid_print()
            time.sleep(0.03)

        while cur_y != initial_y:
            cur_y = cur_y + 3
            grid_print()
            time.sleep(0.03)

        return {cur_x, cur_y}

    elif jump_move == 1:
        temp1 = cur_x + 3
        while cur_y > initial_y - 13:
            cur_y = cur_y - 4
            if cur_x < temp1:
                cur_x = cur_x + 1
            grid_print()
            time.sleep(0.03)
        temp1 = cur_x + 3
        while cur_y != initial_y:
            cur_y = cur_y + 4
            if cur_x < temp1:
                cur_x = cur_x + 1
            grid_print()
            time.sleep(0.03)

        return {cur_x, cur_y}

    elif jump_move == -1:
        temp1 = cur_x - 3
        while cur_y > initial_y - 13:
            cur_y = cur_y - 4
            if cur_x >= temp1:
                cur_x = cur_x - 1
            grid_print()
            time.sleep(0.03)
        temp1 = cur_x - 3
        while cur_y != initial_y:
            cur_y = cur_y + 4
            if cur_x >= temp1:
                cur_x = cur_x - 1
            grid_print()
            time.sleep(0.03)

        return {cur_x, cur_y}


def mario_create(column, row):
    """
        Creates Mario at a particular coordinate
    """

    temp1 = column
    for r in range(4):
        column = temp1
        if row < 80:
            for pixel in range(len(mario_grid[r])):
                grid[row][column] = mario_grid[r][pixel]
                column = column + 1
            row = row + 1

def cloud_print(column,type ):
    temp1 = column
    row = 35
    temp2 = row
    if type == 1:
        for r in range(len(cloud_1)):
            column = temp1
            for k in range(len(cloud_1[r])):
                grid[row][column]  = cloud_1[r][k]
                column = column + 1
            row = row + 1
    elif type == 2:
        for r in range(len(cloud_2)):
            column = temp1
            for k in range(len(cloud_2[r])):
                grid[row][column]  = cloud_2[r][k]
                column = column + 1
            row = row + 1

def pillar_print(column, row, times):

    temp1 = column
    row = row - times - 1

    for r in range(11):
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
#   #0: Normal jump
#   #1: Right jump
#   #-1: Left jump
def grid_bg(pos_symbol, jump_move=0):
    """
        Creates the complete grid with all objects in it
    """
    global cur_x
    global cur_y

    if pos_symbol == 1:
        cur_x = cur_x + 5
        cur_x, cur_y = CheckCollision(cur_x, cur_y, pos_symbol)
        grid_print()

    elif pos_symbol == -1:
        cur_x = cur_x - 5
        cur_x, cur_y = CheckCollision(cur_x, cur_y, pos_symbol)
        grid_print()

    elif pos_symbol == 2:
        jumper(jump_move)
        #cur_x, cur_y = CheckCollision(cur_x, cur_y, pos_symbol)
