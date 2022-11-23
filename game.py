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
player_Rect = player.rect()

playing = True
road, tower_available = Map()
built_tower = []

a = 0
health = 10
step = 0
tower_selected = 0
poker_rand = [0, 0, 0, 0, 0]
poker_card = [[0, 0] for i in range(5)]
changed = [0 for i in range(5)]

while playing:
    SCREEN.fill((0, 0, 0))
    myFont = pygame.font.SysFont("arial", 18, True, False)
    text_Title = myFont.render("Life :"+str(health), True, 'RED')
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 40
    text_Rect.y = 0
    SCREEN.blit(text_Title, text_Rect)
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
                    changed[idx] = 1
                    poker_rand[idx] = random.randint(0, 31)//8
                    shape_ = poker_rand[idx]
                    number_ = poker_rand[idx]%8
                    poker_card[idx][0] = shape_
                    poker_card[idx][1] = number_

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
        a, player_Rect.x, player_Rect.y = move(a, player_Rect)
        a, player_Rect.x, player_Rect.y, health = change_direction(a, player_Rect, SCREEN_WIDTH, health)
        player.show(player_Rect.x, player_Rect.y)
    pygame.display.flip()
    clock.tick(120)
