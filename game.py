import pygame
import random

import game_objs as go
from game_map import Map
from game_card_ranking import card_ranking
from game_move_player import move, change_direction

SCREEN_WIDTH = 26*26
SCREEN_HEIGHT  = 32*26
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame test")

clock = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

Rankings_Tower, tower1 = go.Rankings()
card_img, card_back = go.Cards()
building_complete = go.Building_complete()
road1 = go.Road()
player = go.Player()
red = go.red_Ball()
blue = go.blue_Ball()
exp_1 = go.exp_1()
exp_2 = go.exp_2()
exp_3 = go.exp_3()
exp_4 = go.exp_4()
player_Rect = [player.rect() for i in range(15)]
playing = True
road, tower_available = Map()
built_tower = []
unit = []
round = 1
health = 10
step = 0
tower_selected = 0
poker_rand = [0, 0, 0, 0, 0]
poker_card = [[0, 0] for i in range(5)]
changed = [0 for i in range(5)]
delay = 0
unit_count = 0
unit_health = 5
attack = 10
while playing:
    delay=(delay+1)%120
    SCREEN.fill((0, 0, 0))
    myFont = pygame.font.SysFont("arial", 18, True, False)
    text_Title = myFont.render("Life :"+str(health), True, 'RED')
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 40
    text_Rect.y = 0
    text_Round = myFont.render("Round :"+str(round), True, 'BLUE')
    round_Rect = text_Round.get_rect()
    round_Rect.centerx = 40
    round_Rect.y = 20
    SCREEN.blit(text_Title, text_Rect)
    SCREEN.blit(text_Round, round_Rect)
    for i in range(5):
        if changed[i]:
            red.show(26*i, 26*26)
        else:
            blue.show(26*i, 26*26)
    building_complete.show(613, 0)
    
    for i, j in road:
        MAP_WIDTH, MAP_HEIGHT = SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13
        road1.show(MAP_WIDTH, MAP_HEIGHT)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and (step == 0 or step == 1):
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            for i, j in tower_available:
                if 26*j+13 <= mouse_pos[0] <= 26*j+39 and 26*i+13 <= mouse_pos[1] <= 26*i+39:
                    if step == 1:
                        built_tower.pop()
                    built_tower.append([i, j, 15])
                    tower_selected = [i, j]
                    step = 1
                    break
                
        if event.type == pygame.KEYDOWN and step == 1:
            tower_available.remove(tower_selected)
            step = 2
            
        if step == 2:
            poker_rand = [random.randint(0, 31) for i in range(5)]
            for i in range(5):
                shape = poker_rand[i]//8 # 0=spade, 1=diamond, 2=heart, 3=clover
                number = poker_rand[i]%8
                poker_card[i][0] = shape
                poker_card[i][1] = number
            step = 3
            
        if event.type == pygame.MOUSEBUTTONDOWN and step == 3:
            mouse_pos = pygame.mouse.get_pos()
            card_1st = 0 <= mouse_pos[0] <= 104 and 702 <= mouse_pos[1] <= 808 and changed[0] == 0
            card_2nd = 134 <= mouse_pos[0] <= 238 and 702 <= mouse_pos[1] <= 808 and changed[1] == 0
            card_3rd = 268 <= mouse_pos[0] <= 374 and 702 <= mouse_pos[1] <= 808 and changed[2] == 0
            card_4th = 404 <= mouse_pos[0] <= 508 and 702 <= mouse_pos[1] <= 808 and changed[3] == 0
            card_5th = 538 <= mouse_pos[0] <= 642 and 702 <= mouse_pos[1] <= 808 and changed[4] == 0
            cards = [card_1st, card_2nd, card_3rd, card_4th, card_5th]
            
            for idx, card in enumerate(cards):
                if card:
                    while True:
                        poker_rand[idx] = random.randint(0, 31)//8
                        shape_ = poker_rand[idx]
                        number_ = poker_rand[idx]%8
                        if [shape_, number_] != poker_card[idx]:
                            changed[idx] = 1
                            poker_card[idx][0] = shape_
                            poker_card[idx][1] = number_
                            break

        if event.type == pygame.MOUSEBUTTONDOWN and step == 3:
            mouse_pos = pygame.mouse.get_pos()
            if 613 <= mouse_pos[0] and 0 <= mouse_pos[1] <= 38:
                Rankings_Card = card_ranking(poker_card)
                if True in Rankings_Card:
                    for idx, rank in enumerate(Rankings_Card):
                        if rank == True:
                            built_tower[-1][2] = idx
                else:
                    built_tower[-1][2] = 14
                step = 4
                
    for i, j, k in built_tower:
        TOWER_X, TOWER_Y = SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13
        if k in range(15):
            Rankings_Tower[k].show(TOWER_X, TOWER_Y)
        else:
            tower1.show(TOWER_X, TOWER_Y)
            
    for i in range(5):
        CARD_X, CARD_Y = SCREEN_WIDTH//5*i, SCREEN_WIDTH//26*27
        if step < 3:
            card_back.show(CARD_X, CARD_Y)
        else:
            card_front = card_img[poker_card[i][0]][poker_card[i][1]]
            card_front.show(CARD_X, CARD_Y)
            
    if step == 4:
        if delay==1 and unit_count!=15:
            unit.append([0,unit_count,attack])
            unit_count+=1
        for i in range(len(unit)):
            if unit[i][2]<=0:
                unit[i][0]=-1
        for i in range(len(unit)):
            if unit[i][0]!=-1:
                unit[i][0], player_Rect[i].x, player_Rect[i].y = move(unit[i][0], player_Rect[i])
                unit[i][0], player_Rect[i].x, player_Rect[i].y, health= change_direction(unit[i][0], player_Rect[i], SCREEN_WIDTH, health)
                player.show(player_Rect[i].x, player_Rect[i].y)
        for i,j,k in built_tower:
            for l in range(len(unit)):
                if (player_Rect[l].x!=SCREEN_WIDTH//26*10-1 or player_Rect[l].y!=0) and unit[l][0]!=-1 and ((player_Rect[l].x-19-j*26)-(player_Rect[l].y-19-i*26))**2<=40**2:
                    unit[l][2]-=0.01
                    exp_1.show(26*j+19+0*(player_Rect[l].x-19-26*j)//3,26*i+19+0*(player_Rect[l].y-19-26*i)//3)
                    exp_2.show(26*j+19+1*(player_Rect[l].x-19-26*j)//3,26*i+19+1*(player_Rect[l].y-19-26*i)//3)
                    exp_3.show(26*j+19+2*(player_Rect[l].x-19-26*j)//3,26*i+19+2*(player_Rect[l].y-19-26*i)//3)
                    exp_4.show(26*j+19+3*(player_Rect[l].x-19-26*j)//3,26*i+19+3*(player_Rect[l].y-19-26*i)//3)
                    break
        if len(unit)==15 and sorted(unit,key=lambda x : -x[0])[0][0]==-1:
            step=0
            unit_count=0
            unit=[]
            poker_rand = [0, 0, 0, 0, 0]
            poker_card = [[0, 0] for i in range(5)]
            changed = [0 for i in range(5)]
            player_Rect = [player.rect() for i in range(15)]
            round+=1
            unit_health*=1.15
    pygame.display.flip()
    clock.tick(120)
