#CONTAINS GENERATE, PRINT AND UPDATE FUNCTIONS FOR ALL OBSTACLES IN THE GAME
import random
from colorama import *
import sys
import os
from classes import *
from collision import CheckCollision

o.grid[:31, :93, :1] = ' '

class Gen_Col:
    """GENERATES RANDOM NUMBER AND ASSIGNS COLOR FOR OBJECTS"""

    __color = {"coin": "YELLOW", "cloud":"BLUE", "bridge": "MAGENTA", "pillar": "CYAN", "alien": "GREEN"}
    def __init(self):
        number = 0

    def num_gen(self, limit1, limit2):

        if limit2 == 1:
            return random.random()
        else:
            return random.randint(limit1, limit2)

    def col_gen(self, obj):

        return self.__color[str(obj)]

class Generators(Gen_Col):
    """GENERATES OBJECTS RANDOMLY BASED ON RANDOM NUMBER. INHERITS ABOVE CLASS"""

    def coin_engine(self):

        make = Gen_Col.num_gen(self, 0,1)

        if make > 0.5:
            if len(o.live_coins) == 0:
                o.live_coins.append(80)
            else:
                if o.live_coins[len(o.live_coins) -1] + 10 <80:
                    o.live_coins.append(80)

    def cloud_engine(self):
        type = Gen_Col.num_gen(self, 0,3)

        if len(o.live_cloud) == 0:
            o.live_cloud.append([80,type])

        if len(o.live_cloud) > 0:
            if o.live_cloud[len(o.live_cloud) -1][0] +  10 < 80 :
                o.live_cloud.append([80,type])

    def pillar_engine(self):

        pillar_height = Gen_Col.num_gen(self, 3,9)
        pillar_gen = Gen_Col.num_gen(self, 0,100)
        if pillar_gen >90:
            if len(o.live_pillars) == 0 :
                o.live_pillars.append([80,pillar_height])

            if len(o.live_pillars) > 0 :
                if len(o.live_aliens)==0 and o.live_pillars[len(o.live_pillars) -1][0] +  20 < 80:
                    o.live_pillars.append([80,pillar_height])
                elif len(o.live_aliens) >0 and o.live_aliens[len(o.live_aliens)-1][0] + 20 < 80:
                    o.live_pillars.append([80,pillar_height])
                else:
                    pass

    def alien_engine(self):

        mean = 3

        if len(o.live_aliens) == 0 and len(o.live_pillars)>0 and o.live_pillars[len(o.live_pillars) -1][0] +  20 < 80 :
            o.live_aliens.append([80, mean])

        if len(o.live_aliens) > 0 and len(o.live_pillars)>0:
            if o.live_aliens[len(o.live_aliens) -1][0] +  10 < 80 and o.live_pillars[len(o.live_pillars) -1][0] +  20 < 80 :
                o.live_aliens.append([80, mean])


    def mega_alien_engine(self):

        if len(o.live_mega_aliens) == 0 and len(o.live_pillars)>0 and o.live_pillars[len(o.live_pillars) -1][0] +  20 < 80 :
            o.live_mega_aliens.append([80,31])

    def bridge_engine(self):

        blocks = Gen_Col.num_gen(self, 2,5)
        bridge_gen = Gen_Col.num_gen(self, 0,100)
        if bridge_gen > 90:
            o.live_bridge.append([80, blocks])


class Print_Fn(Gen_Col):
    """PRINTS ALL THE OBJECTS ON TO THE BOARD"""

    def coin_print(self):

        row = 20
        for coin in o.live_coins:
            o.grid[row][coin][0] = '$'
            o.grid[row][coin][1] = Gen_Col.col_gen(self, "coin")
    def cloud_print(self):

        for cloud in range(len(o.live_cloud)):
            column = o.live_cloud[cloud][0]
            type = o.live_cloud[cloud][1]

            temp1 = column
            row = 2
            temp2 = row

            if type == 1:
                for r in range(len(o.cloud_1)):
                    column = temp1
                    for k in range(len(o.cloud_1[r])):
                        o.grid[row][column][0] = o.cloud_1[r][k]
                        o.grid[row][column][1] = Gen_Col.col_gen(self, "cloud")
                        column = column + 1
                    row = row + 1

            elif type == 2:
                for r in range(len(o.cloud_2)):
                    column = temp1
                    for k in range(len(o.cloud_2[r])):
                        o.grid[row][column][0] = o.cloud_2[r][k]
                        o.grid[row][column][1] = Gen_Col.col_gen(self, "cloud")
                        column = column + 1
                    row = row + 1


    def bridge_print(self):

        for bri in range(len(o.live_bridge)):

            column = o.live_bridge[bri][0]
            row = 15
            temp = o.live_bridge[bri][0]
            for i in range(o.live_bridge[bri][1]):
                for j in range(len(o.bridge)):
                    for k in range(len(o.bridge[j])):
                        o.grid[row][column][0] = o.bridge[j][k]
                        o.grid[row][column][1] = Gen_Col.col_gen(self, "bridge")
                        column = column + 1
                    row = row + 1
                    column = temp
                row = 15
                temp = o.live_bridge[bri][0] + 6
                column = temp


    def pillar_print(self):

        for pil in range(len(o.live_pillars)):

            column = o.live_pillars[pil][0]
            temp1 = column
            row = 31 - o.live_pillars[pil][1]
            times = o.live_pillars[pil][1]

            for r in range(11):
                o.grid[row][column][0] = o.pillar_top[0][r]
                o.grid[row][column][1] = Gen_Col.col_gen(self, "pillar")
                column = column + 1

            column = temp1
            row = row + 1

            for r in range(times):
                column = temp1
                for pixel in range(len(o.pillar_side[0])):
                    o.grid[row][column][0] = o.pillar_side[0][pixel]
                    column = column + 1
                row = row + 1


    def alien_print(self):

        for ali in range(len(o.live_aliens)):

            column = o.live_aliens[ali][0]
            temp1 = column
            row = 31 - 1

            for r in range(len(o.alien)):
                for k in range(len(o.alien[r])):
                    o.grid[row][column][0] = o.alien[r][k]
                    o.grid[row][column][1] = Gen_Col.col_gen(self, "alien")
                    column = column + 1
                row = row + 1
                column = temp1

    def mega_alien_print(self):

        if len(o.live_mega_aliens) == 1:
            row = o.live_mega_aliens[0][1] - len(o.mega_alien) + 1
            for r in range(len(o.mega_alien)):
                column = o.live_mega_aliens[0][0]
                for c in range(len(o.mega_alien[r])):
                    o.grid[row][column][0] = o.mega_alien[r][c]
                    o.grid[row][column][1] = Gen_Col.col_gen(self,"alien")
                    column = column + 1
                row = row + 1

class Update_Fn:
    """UPDATES ALL THE X, Y COORDINATES OF ALL OBJECTS"""
    
    def coin_update(self, move_1, move_2):

        del_coins=[]
        step = 3
        if move_1 == 1 or move_2 == 1:
            for coin in range(len(o.live_coins)):
                if o.live_coins[coin]<10:
                    try:
                        del_coins.remove(o.live_coins[coin])
                    except:
                        pass
                else:
                    o.live_coins[coin] = o.live_coins[coin] - step
                    del_coins.append(o.live_coins[coin])

            del o.live_coins[:]
            for coin in range(len(del_coins)):
                o.live_coins.append(del_coins[coin])

    def cloud_update(self, move_1, move_2):

        del_cloud=[]
        step = 4

        if move_1 == 1 or move_2 == 1:
            for cloud in range(len(o.live_cloud)):
                if o.live_cloud[cloud][0]<10:
                    try:
                        del_cloud.remove(o.live_cloud[cloud])
                    except:
                        pass
                else:
                    o.live_cloud[cloud][0] = o.live_cloud[cloud][0] - step

                    del_cloud.append(o.live_cloud[cloud])


            del o.live_cloud[:]

            for cloud in range(len(del_cloud)):
                o.live_cloud.append(del_cloud[cloud])

    def pillar_update(self, move_1, move_2):

        del_pillars=[]
        step = 3
        if move_1 == 1 or move_2 == 1:
            for pillar in range(len(o.live_pillars)):
                if o.live_pillars[pillar][0]<10:
                    try:
                        del_pillars.remove(o.live_pillars[pillar])
                    except:
                        pass
                else:
                    o.live_pillars[pillar][0] = o.live_pillars[pillar][0] - step

                    del_pillars.append(o.live_pillars[pillar])


            del o.live_pillars[:]
            for pillar in range(len(del_pillars)):
                o.live_pillars.append(del_pillars[pillar])


    def alien_update(self, move_1, move_2, cur_x, cur_y, on_air):

        del_aliens=[]
        step = 2

        if move_1 == 1 or move_2 == 1:
            for alien in range(len(o.live_aliens)):
                if o.live_aliens[alien][0]<10:
                    try:
                        del_aliens.remove(o.live_aliens[alien])
                    except:
                        pass
                else:
                    o.live_aliens[alien][0] = o.live_aliens[alien][0] - step

                    del_aliens.append(o.live_aliens[alien])

            del o.live_aliens[:]
            for alien in range(len(del_aliens)):
                o.live_aliens.append(del_aliens[alien])
        else:

            for alien in range(len(o.live_aliens)):
                if o.live_aliens[alien][0] + 7 >= cur_x and cur_x + 6 >= o.live_aliens[alien][0]  and cur_y == 31 and on_air == 0:
                    m.life = m.life - 1
                    m.cur_y = m.cur_y - 12
                    if m.life == 0:
                        print(Fore.RESET + Style.RESET_ALL+"\t \t \t \t \tGAME OVER")
                        os.system('aplay -q smb_mariodie.wav&')
                        sys.exit()
                    return 1

                elif o.live_aliens[alien][0] - 1 <= cur_x + 6 and o.live_aliens[alien][0] + 7 >= cur_x and cur_y == 31 and on_air == 0:
                    m.life = m.life - 1
                    m.cur_y = m.cur_y - 12
                    if m.life == 0:
                        print(Fore.RESET + Style.RESET_ALL+"\t \t \t \t \tGAME OVER")
                        os.system('aplay -q smb_mariodie.wav&')
                        sys.exit()
                    return 1

                elif o.live_aliens[alien][1] > 0 and o.live_aliens[alien][0] + 7 + step < 93:
                    if np.all(o.grid[29: 31, o.live_aliens[alien][0] + 7 : o.live_aliens[alien][0] + 7 + step, 0:1] == ' ') or o.live_aliens[alien][0] + 7 + step >=cur_x :
                        o.live_aliens[alien][0] = o.live_aliens[alien][0] + step
                        o.live_aliens[alien][1] = o.live_aliens[alien][1] - 1
                elif o.live_aliens[alien][1] > -3 and o.live_aliens[alien][0] - step - 1 >0:
                    if np.all(o.grid[29:31, o.live_aliens[alien][0] - step - 1: o.live_aliens[alien][0] , 0:1] == ' ') or o.live_aliens[alien][0] - step -1 <=cur_x + 6:
                        o.live_aliens[alien][0] = o.live_aliens[alien][0] - step
                        o.live_aliens[alien][1] = o.live_aliens[alien][1] - 1
                else:
                    pass

                if o.live_aliens[alien][1] == -3:
                    o.live_aliens[alien][1] = 3
        return 0

    def mega_alien_update(self, cur_x, cur_y):

        step = 2
        if len(o.live_mega_aliens)>0:
            # print(o.live_mega_aliens[0][1])
            if cur_x < o.live_mega_aliens[0][0]:
                if np.all(o.grid[o.live_mega_aliens[0][1] - len(o.mega_alien) + 1: o.live_mega_aliens[0][1] + 1, o.live_mega_aliens[0][0] - 1 - 3: o.live_mega_aliens[0][0], 0:1] == ' '):
                    o.live_mega_aliens[0][0] = o.live_mega_aliens[0][0] - step
                elif o.live_mega_aliens[0][1] - len(o.mega_alien) - step > 0:
                    o.live_mega_aliens[0][1] = o.live_mega_aliens[0][1] - step
                return 0
            elif cur_x >= o.live_mega_aliens[0][0]:
                if np.all(o.grid[31 - len(o.mega_alien): 32, o.live_mega_aliens[0][0] + 10: o.live_mega_aliens[0][0] + 10 + step, 0:1] == ' '):
                    o.live_mega_aliens[0][0] = o.live_mega_aliens[0][0] + step
                elif o.live_mega_aliens[0][1] - len(o.mega_alien) -  step > 0:
                    o.live_mega_aliens[0][1] = o.live_mega_aliens[0][1] - step
                return 1
            else:
                pass

    def bridge_update(self, move_1, move_2):

        del_bridge=[]
        step = 3
        if move_1 == 1 or move_2 == 1:
            for bridge in range(len(o.live_bridge)):
                if o.live_bridge[bridge][0]<10:
                    try:
                        del_bridge.remove(o.live_bridge[bridge])
                    except:
                        pass
                else:
                    o.live_bridge[bridge][0] = o.live_bridge[bridge][0] - step

                    del_bridge.append(o.live_bridge[bridge])


            del o.live_bridge[:]
            for bridge in range(len(del_bridge)):
                o.live_bridge.append(del_bridge[bridge])

g = Generators()
p = Print_Fn()
u = Update_Fn()
