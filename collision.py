

def CheckCollision(cur_x, cur_y, pos_symbol):

    if pos_symbol == 1 and cur_x == 45:
        return 40, cur_y;
    elif pos_symbol == -1 and cur_x == -5:
        return 0, cur_y;
    else:
        return cur_x, cur_y;
