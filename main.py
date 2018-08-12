import os
import sys
import time
from input import Get,input_to
from creator import grid_bg, cur_x, cur_y
from generator import gen_engine, pillar_update
from colorama import *

init()

getch = Get()
grid_bg(0)

def mario_move(input):

    if input == 'd':
        pillar_update(1)
        grid_bg(1)

    elif input == 'a':
        pillar_update(0)
        grid_bg(-1)

    elif input == 'w':
        pillar_update(0)
        grid_bg(2)

    else:
        pillar_update(0)
        grid_bg(0)


while True:
    input = input_to(getch)
    os.system('clear')
    print(Back.RESET)
    print(Style.RESET_ALL)
    grid_bg(0)

    if input == 'q':
        print(Back.RESET)
        deinit()
        os.system('clear')
        sys.exit()

    else:
        gen_engine(cur_x)
        mario_move(input)

    time.sleep(0.0666)

"""
SUPER MARIO

────▄████▄▄
───▄▀█▀▐└─┐
───█▄▐▌▄█▄┘
───└▄▄▄▄─┘
▄███▒██▒███▄
▒▒█▄▒▒▒▒▄█▒▒
──▒▒▒▀▀▒▒▒
▄███────███▄
"""
