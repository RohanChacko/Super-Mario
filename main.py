import os
import sys
import time
from input import Get, input_to
from creator import grid_bg, grid_print
from classes import *
from colorama import *
from generator import *


while m.level!= '1' and m.level != '2' and m.level != '3':
    print("Input level of difficulty required [1, 2, 3]")
    m.level = input()

m.level = int(m.level)
getch = Get()
p.pillar_print()
p.bridge_print()
p.cloud_print()
m.mario_print()

grid_print()

while True:
    input = input_to(getch)

    move_1 = 0
    move_2 = 0

    if input is not None:

        if input == 'q' or m.score == 30 and m.level == 3:
            print(Fore.RESET + Style.RESET_ALL+"\t \t \t \t YOU SCORED: "+str(m.score)+ " | GAME OVER")
            os.system('aplay -q sounds/smb_gameover.wav&')
            sys.exit()

        elif input == 'w':
            move_1 = 2
            jump_input = input_to(getch)

            if jump_input == 'd':
                move_2 = 1
            elif jump_input == 'a':
                move_2 = -1
            else:
                move_2 = 0

        elif input == 'd':
            move_1 = 1
        elif input == 'a':
            move_1 = -1
        else:
            pass

        if m.score >= 20 and m.level == 2:
            os.system('aplay -q sounds/smb_flagpole.wav')
            m.score = 0
            m.level = 3
        elif m.score >= 10 and m.level == 1:
            os.system('aplay -q sounds/smb_flagpole.wav')
            m.score = 0
            m.level = 2
    grid_bg(move_1, move_2)
    time.sleep(0.02)
