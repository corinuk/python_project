def move(a, player_Rect):
    if a % 4 == 0:
        player_Rect.y += 1
    elif a % 4 == 1:
        player_Rect.x -= 1
    elif a % 4 == 2:
        player_Rect.y -= 1
    elif a % 4 == 3:
        player_Rect.x += 1
    return a, player_Rect.x, player_Rect.y

def change_direction(a, player_Rect, SCREEN_WIDTH, health):
        if player_Rect.bottom > SCREEN_WIDTH//26*24+13 and (a == 0 or a == 4):
            a += 1
            player_Rect.y -= 1
        elif player_Rect.left < SCREEN_WIDTH//26*2+13 and (a == 1 or a == 9):
            a += 1
            player_Rect.x += 1
        elif player_Rect.top < SCREEN_WIDTH//26*14+13 and a == 2:
            a += 1
            player_Rect.y += 1
        elif player_Rect.right > SCREEN_WIDTH//26*23+13 and a == 3:
            a += 1
            player_Rect.x -= 1
        elif player_Rect.left < SCREEN_WIDTH//26*15+13 and a == 5:
            a += 1
            player_Rect.y -= 1
        elif player_Rect.top < SCREEN_WIDTH//26*2+13 and (a == 6 or a == 10):
            a += 1
            player_Rect.x += 1
        elif player_Rect.right > SCREEN_WIDTH//26*23+13 and a == 7:
            a += 1
            player_Rect.y += 1
        elif player_Rect.bottom > SCREEN_WIDTH//26*12+13 and a == 8:
            a += 1
            player_Rect.x -= 1
        elif player_Rect.right > SCREEN_WIDTH//26*13+13 and a == 11:
            a += 1
            player_Rect.y -= 1
        elif player_Rect.bottom > SCREEN_WIDTH//26*26+13 and a == 12:
            health -= 1
            a = 0.1
        return a, player_Rect.x, player_Rect.y, health
