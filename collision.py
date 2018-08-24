from classes import *
import numpy as np
import os
import sys

def CheckCollision(cur_x, cur_y, reach_max, on_air, move_1, move_2):
    """COLLISION CHECKER"""

    pil_col = 0
    step = 3
    update_flag = 1
    increment_x = step * move_1
    increment_y = step * move_2

    if move_1 == 1:

        if np.all(o.grid[cur_y -3  : cur_y + 1, cur_x + 7: cur_x + 7 + step, 0:1] == ' ') :
            return 0, 1
        else:
            return 0, -1

    elif move_1 == -1:

        if np.all(o.grid[ cur_y -3  : cur_y + 1, cur_x - step: cur_x, 0:1] == ' ') :
            return 0, 1
        else:
            return 0, -1

    elif move_1 == 2:
        if move_2 == 0 and reach_max == 0:
            if np.all(o.grid[cur_y - 3 - step : cur_y - 3, cur_x : cur_x + 7, 0:1] == ' ') or len(o.live_mega_aliens) >0 and cur_y - 3 - step <= o.live_mega_aliens[0][1]:
                return 1, 1
            else:
                return 1, -1
        elif move_2 == 0 and reach_max == 1:
            if np.all(o.grid[ cur_y + 1 : cur_y + step + 1 , cur_x : cur_x + 7, 0:1] == ' ') :
                return 1, 1
            else:
                return 1, -1

        elif move_2 == 1 and reach_max == 0:
            if np.all(o.grid[cur_y - 3 - step : cur_y - 3, cur_x + 7 : cur_x + 7+ step, 0:1] == ' ') or len(o.live_mega_aliens) >0 and cur_y - 3 - step <= o.live_mega_aliens[0][1] :
                return 1, 1
            else:
                return 1, -1

        elif move_2 == 1 and reach_max == 1:
            if np.all(o.grid[cur_y + 1 : cur_y + step + 1 , cur_x + 7: cur_x + 7 + step, 0:1] == ' ') :
                return 1, 1
            else:
                return 1, -1

        elif move_2 == -1 and reach_max == 0:
            if np.all(o.grid[cur_y - 3 - step : cur_y - 3, cur_x - step: cur_x, 0:1] == ' ') :
                return 1, 1
            else:
                return 1, -1

        elif move_2 == -1 and reach_max == 1:
            # print(o.grid[cur_y + 1 : cur_y + step + 1, cur_x - step: cur_x].shape)
            if np.all(o.grid[cur_y + 1 : cur_y + step + 1, cur_x - step: cur_x, 0:1] == ' ') :
                return 1, 1
            else:
                return 1, -1
    else:
        return on_air, 0

def alien_collision(cur_x, cur_y):
    """ALIEN COLLISION CHECKER"""
    
    for alien in o.live_aliens:
        if cur_x >=alien[0] and cur_x + 6 <= alien[0] + 7 and cur_y == 31:
            print(Fore.RESET + Style.RESET_ALL+"\t \t \t \t \tGAME OVER")
            sys.exit()
