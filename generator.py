import random
from colorama import *

init()


pillar_top = ["==========="]
pillar_side = ["||       ||"]

live_pillars = []
live_aliens = []

def gen_engine(cur_x):
    pillar_height = random.randint(3, 9)
    pillar_gen = random.randint(0,100)
    if pillar_gen >90:
        live_pillars.append([80,pillar_height])


def pillar_update(input):
    global live_pillars
    del_pillars=[]

    if input == 1:
        for pillar in range(len(live_pillars)):
            if live_pillars[pillar][0]<10:
                try:
                    del_pillars.remove(live_pillars[pillar])
                except:
                    pass
            else:
                live_pillars[pillar][0] = live_pillars[pillar][0] - 10
                del_pillars.append(live_pillars[pillar])


        del live_pillars[:]
        for pillar in range(len(del_pillars)):
            live_pillars.append(del_pillars[pillar])
