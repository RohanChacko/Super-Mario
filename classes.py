import numpy as np


class Mario:
    """DEFINES ALL MARIO VARIABLES AND FUNCTIONS"""

    def __init__(self):

        self.cur_x = 0
        self.cur_y = 31
        self.on_air = 0
        self.reach_max = 0
        self.mario_grid = ["   |   ", " (' ') ", "/|; ;|\\", "  / \  "]
        self.past_step = 0
        self.perm = 0  # Helps in storing coordinates temporarily in functions
        self.step = 3
        self.score = 0
        self.level = 1
        self.life = 3
        self.level_thresh = {'1': [90, 60, 30], '2': [80, 60, 40], '3': [70, 60, 50]}

    def mario_update(self, move_1, cur_x, update_flag):

        step = 3

        if cur_x + move_1 * step < 40:

            if move_1 == 1:
                cur_x = cur_x + step
            elif move_1 == -1:
                cur_x = cur_x - step

                if cur_x < 0:
                    cur_x = cur_x + step

        return cur_x

    def mario_print(self):
        """
            Creates Mario at a particular coordinate
        """
        column = m.cur_x
        row = m.cur_y
        temp1 = column
        row = row - 3

        for r in range(4):
            column = temp1
            if row < 40:
                for pixel in range(len(m.mario_grid[r])):
                    o.grid[row][column][0] = m.mario_grid[r][pixel]
                    o.grid[row][column][1] = "YELLOW"
                    column = column + 1
                row = row + 1


class Objects:
    """ASCII ART FOR ALL OBJECTS AND HAS LIST OF ALL OBJECTS ON SCREEN"""
    
    def __init__(self):

        self.pillar_top = ["==========="]
        self.pillar_side = ["|||||||||||"]
        self.cloud_1 = ["       _        ", "      ( )_      ", "    ( `   )_    ",
                        "  (    )  ( `)  ", "(__  (_ .  _) _)"]
        self.cloud_2 = ["   __   _   ", " _(  )_( )_ ", "(_   _    _)", "  (_) (__)  "]
        self.bridge = ["======", "|    |", "|    |", "======"]
        self.alien = ["_/*_*\_", "---/\--"]
        self.mega_alien = ["  [\V/] ",
                           " (0 & 0)", "/(|___|)\\ ", "  ///\\\\\\"]

        self.grid = np.zeros(shape=(40, 93, 2), dtype=object)

        self.live_bridge = []
        self.live_pillars = []
        self.live_aliens = []
        self.live_mega_aliens = []
        self.live_cloud = []
        self.live_coins = []

m = Mario()
o = Objects()
