import numpy as np
import time
import sys
import os
from colorama import *
from collision import CheckCollision, alien_collision
import random
from generator import *
from classes import *


################################################################################

def grid_print():
    """PRINT THE GRID ONTO THE SCREEN"""
    sys.stdout.flush()
    try:
        os.system('clear')
    except BaseException:
        os.system('cls')

    print(Fore.RESET+"Lives: " + str(m.life) + "\t \t \t \tScore: " + str(m.score)+ "\t \t \t \tLevel: "+str(m.level))
    for row in range(np.size(o.grid, 0)):
        for column in range(np.size(o.grid, 1)):
            if o.grid[row][column][0] != ' ' and o.grid[row][column][0] != 0:
                if o.grid[row][column][1] == ' ':
                    o.grid[row][column][1] = "BLUE"
                sys.stdout.write(getattr(Fore, o.grid[row][column][1]) + Style.BRIGHT + str(o.grid[row][column][0]))
            elif row <= 31:
                sys.stdout.write(Fore.RESET+Style.RESET_ALL+' ')
            if row > 31:
                sys.stdout.write(Fore.RED+Style.BRIGHT+"L")
        sys.stdout.write("\n")

def jumper(jump_move):
    """MARIO JUMPS INCREMENTALLY"""
    if m.on_air == 0:
        m.perm = m.cur_y
        m.on_air = 1
        m.reach_max = 0

    m.step = 3
    if jump_move == 0:

        if m.cur_y > m.perm - 12 and m.reach_max == 0:

            coin_catch(jump_move)
            m.on_air, update_flag = CheckCollision(
                m.cur_x, m.cur_y, 0, 0, 2, 0)
            if update_flag == 1:
                m.cur_y = m.cur_y - m.step
            else:
                m.reach_max = 1
            return

        m.reach_max = 1
        if m.cur_y <= m.perm and m.reach_max == 1:
            m.on_air, update_flag = CheckCollision(
                m.cur_x, m.cur_y, 1, 0, 2, 0)
            if update_flag == 1:
                m.cur_y = m.cur_y + m.step

        if m.cur_y >= m.perm:
            m.on_air = 0

    elif jump_move == 1:

        if m.cur_y > m.perm - 12 and m.reach_max == 0:

            coin_catch(jump_move)
            m.on_air, update_flag = CheckCollision(
                m.cur_x, m.cur_y, 0, m.on_air, 2, jump_move)

            if update_flag == 1:
                u.bridge_update(2, jump_move)
                u.pillar_update(2, jump_move)
                u.alien_update(2, jump_move, m.cur_x, m.cur_y, m.on_air)
                u.mega_alien_update(m.cur_x, m.cur_y)
                u.coin_update(2, jump_move)
                u.cloud_update(2, jump_move)
                m.cur_y = m.cur_y - m.step
            else:
                m.reach_max = 1

            return

        m.reach_max = 1
        if m.cur_y <= m.perm and m.reach_max == 1:
            m.on_air, update_flag = CheckCollision(
                m.cur_x, m.cur_y, 1, m.on_air, 2, jump_move)

            if update_flag == 1:
                u.bridge_update(2, jump_move)
                u.pillar_update(2, jump_move)
                u.alien_update(2, jump_move, m.cur_x, m.cur_y, m.on_air)
                u.mega_alien_update(m.cur_x, m.cur_y)
                u.coin_update(2, jump_move)
                u.cloud_update(2, jump_move)
                m.cur_y = m.cur_y + m.step
            else:
                m.on_air = 0

        if m.cur_y >= m.perm:
            m.on_air = 0

    elif jump_move == -1:

        if m.cur_y > m.perm - 12 and m.reach_max == 0:
            coin_catch(jump_move)
            m.on_air, update_flag = CheckCollision(
                m.cur_x, m.cur_y, 0, m.on_air, 2, jump_move)

            if update_flag == 1:
                m.cur_y = m.cur_y - m.step
                m.cur_x = m.mario_update(-1, m.cur_x, update_flag)
            else:
                m.reach_max = 1

            return

        m.reach_max = 1
        if m.cur_y <= m.perm and m.reach_max == 1:
            m.on_air, update_flag = CheckCollision(
                m.cur_x, m.cur_y, 1, m.on_air, 2, jump_move)

            if update_flag == 1:
                m.cur_y = m.cur_y + m.step
                m.cur_x = m.mario_update(-1, m.cur_x, update_flag)
            else:
                m.on_air = 0

        if m.cur_y >= m.perm:
            m.on_air = 0

    else:
        pass

def coin_catch(move):
    """CAPTURING COINS"""
    if move == 0:
        x = 0
    elif move == 1:
        x = 3
    else:
        move = -3
    for coin in range(len(o.live_coins)):
        if m.cur_y - m.step >= 20 and m.cur_y - m.step - 4 <= 20 and m.cur_x + move <= o.live_coins[coin] and m.cur_x +move+ 6 >= o.live_coins[coin]:
            m.score+=1
            os.system('aplay -q sounds/smb_coin.wav&')
            o.grid[20][o.live_coins[coin]][0] = ' '
            del o.live_coins[coin]
            break

    p.coin_print()

def alien_destroy():
    """DESTROY ALIENS BY JUMPING ON THEM"""
    flag = 0

    if len(o.live_aliens) > 0:

        for alien in range(len(o.live_aliens)):
            if m.cur_y == 29 and m.cur_x + 7 >= o.live_aliens[alien][0] and m.cur_x <= o.live_aliens[alien][0] + 6:
                o.grid[30: 32, o.live_aliens[alien][0]: o.live_aliens[alien][0] + 8, 0:1] = ' '
                m.score+=2
                del o.live_aliens[alien]
                flag = 1
                break

        if flag == 1:
            m.cur_y = 31

    return flag


def lower(lol):
    """LOWER Y-COORDINATE OF MARIO"""

    temp1 = m.cur_y
    if m.cur_y < 31:
        final_y = m.cur_y
        while np.all(o.grid[final_y + 1: final_y + 2, m.cur_x: m.cur_x + 7, 0:1] == ' '):
            m.cur_y = final_y + 1
            final_y = final_y + 1

    alien_destroy()
    return m.cur_y

def mega_alien_destroy():
    """DESTROY BOSS ALIEN"""

    flag = 0
    step = 3

    if len(o.live_mega_aliens) > 0:
        if m.cur_y <= o.live_mega_aliens[0][1] - len(o.mega_alien) - 1 - step and m.cur_x + 7 >= o.live_mega_aliens[0][0] and m.cur_x <= o.live_mega_aliens[0][0] + 9:
            del o.live_mega_aliens[0]
            m.score+=5
            flag = 1

        if flag == 1:
            m.cur_y = 31

def alien_lower():
    """LOWERS BOSS ALIEN"""

    if len(o.live_mega_aliens) >0:
        temp1 = o.live_mega_aliens[0][1]
        if o.live_mega_aliens[0][1] < 31:
            final_y = o.live_mega_aliens[0][1]
            while np.all(o.grid[final_y + 1: final_y + 2, m.cur_x: m.cur_x + 10, 0:1] == ' '):
                o.live_mega_aliens[0][1] = final_y + 1
                final_y = final_y + 1
    mega_alien_destroy()


def grid_bg(move_1, move_2):
    """DECIDES WHICH FUNCTION TO CALL WHEN INPUT IS RECEIVED"""

    m.step = 3

    if m.on_air == 1:
        jumper(m.past_step)
    elif move_1 == 2 and m.on_air == 0:
        m.past_step = move_2
        os.system('aplay -q sounds/smb_jump-small.wav&')
        jumper(m.past_step)

    else:
        m.on_air, update_flag = CheckCollision(
            m.cur_x, m.cur_y, -1, m.on_air, move_1, move_2)

        if update_flag == 1:
            if m.cur_x + move_1 * m.step >= 40:
                toggle = random.randint(0, 100)
                if toggle > m.level_thresh[str(m.level)][0]:
                    g.pillar_engine()
                elif toggle > m.level_thresh[str(m.level)][1]:
                    g.bridge_engine()
                elif toggle > m.level_thresh[str(m.level)][2]:
                    g.alien_engine()
                    g.mega_alien_engine()
                else:
                    g.coin_engine()
                g.cloud_engine()

                u.bridge_update(move_1, move_2)
                u.pillar_update(move_1, move_2)
                u.cloud_update(move_1, move_2)
                u.coin_update(move_1, move_2)
            else:
                m.cur_x = m.mario_update(move_1, m.cur_x, update_flag)

    new_life = u.alien_update(move_1, move_2, m.cur_x, m.cur_y, m.on_air)
    low_alien = u.mega_alien_update(m.cur_x, m.cur_y)


    if m.on_air == 0:
        lower(m.cur_y)

    if new_life == 1:
        lower(m.cur_y)
    if low_alien == 1:
        alien_lower()


    # RESET GRID
    o.grid[ :32, :93, :2] = ' '
    p.pillar_print()
    p.bridge_print()
    p.alien_print()
    p.mega_alien_print()
    p.coin_print()
    p.cloud_print()

    m.mario_print()
    grid_print()
