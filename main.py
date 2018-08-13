import os
import sys
import time
from input import Get,input_to
from creator import grid_bg, grid_print, cur_x, cur_y
from generator import gen_engine, pillar_update, cloud_engine, cloud_update
from colorama import *

init()

getch = Get()
grid_print()
jump = 0
def mario_move(input, input2):

    if input == 'd':
        pillar_update(1, input2)
        cloud_update(1, input2)
        grid_bg(1, 0)

    elif input == 'a':
        pillar_update(0, input2)
        cloud_update(0, input2)
        grid_bg(-1, 0)

    elif input == 'w':
        pillar_update(0, input2)
        cloud_update(0, input2)
        grid_bg(2, input2)
    else:
        pass

while True:
    input = input_to(getch)

    if input is not None:

        os.system('clear')

        if input == 'q':
            os.system('clear')
            sys.exit()

        elif input == 'w':
            jump_input = input_to(getch)

            if jump_input == 'd':
                mario_move(input,1)
            elif jump_input == 'a':
                mario_move(input,-1)
            else:
                mario_move(input,0)
        elif input == 'd' or input == 'a':
            gen_engine()
            cloud_engine()
            mario_move(input,0)

        else:
            grid_print()

        time.sleep(0.0999)
