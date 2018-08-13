import random
from colorama import *

init()


pillar_top = ["==========="]
pillar_side = ["||       ||"]

live_pillars = []
live_aliens = []


cloud_1 = ["  ###### ", " ####### ", " ########", "#########", " ######### ", " ####### "]
cloud_2 = [" ##### ", "#######","  #### "]

live_cloud = []

def cloud_engine():
    type = random.randint(0,3)
    live_cloud.append([80,type])

def cloud_update(input, input2):
    global live_cloud
    del_cloud=[]

    if input == 1 or input2 == 1:
        for cloud in range(len(live_cloud)):
            if live_cloud[cloud][0]<10:
                try:
                    del_cloud.remove(live_cloud[cloud])
                except:
                    pass
            else:
                live_cloud[cloud][0] = live_cloud[cloud][0] - 10
                del_cloud.append(live_cloud[cloud])


        del live_cloud[:]

        for cloud in range(len(del_cloud)):
            live_cloud.append(del_cloud[cloud])

def gen_engine():
    pillar_height = random.randint(3, 9)
    pillar_gen = random.randint(0,100)
    if pillar_gen >90:
        live_pillars.append([80,pillar_height])


def pillar_update(input, input2):
    global live_pillars
    del_pillars=[]

    if input == 1 or input2 == 1:
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
