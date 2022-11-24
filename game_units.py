from game_move_player import Move, Change_direction
import game_objs as go

exp = go.Exp()
SCREEN_WIDTH=26*26

def Die(unit, i):
    unit_die = unit[i][0]
    if unit[i][2] <= 0:
        unit_die = -1
    return unit_die

def Move_units(unit, i, player, player_Rect, health):
    unit[i][0], player_Rect[i].x, player_Rect[i].y = Move(unit[i][0], player_Rect[i])
    unit[i][0], player_Rect[i].x, player_Rect[i].y, health = Change_direction(unit[i][0], player_Rect[i], SCREEN_WIDTH, health)
    player.show(player_Rect[i].x, player_Rect[i].y)
    return unit[i][0], health

def Attack_unit(unit, i, j, player_Rect):
    for l in range(len(unit)):
        ATTACK_CONDITION = player_Rect[l].x != SCREEN_WIDTH//26*10-1 or player_Rect[l].y != 0
        ATTACK_RANGE = unit[l][0]!=-1 and ((player_Rect[l].x-19-j*26)-(player_Rect[l].y-19-i*26))**2<=40**2
        if ATTACK_CONDITION and ATTACK_RANGE:
            unit[l][2]-=0.1
            for m in range(len(exp)):
                exp[m].show(26*j+19+m*(player_Rect[l].x-19-26*j)//3,26*i+19+m*(player_Rect[l].y-19-26*i)//3)
            break