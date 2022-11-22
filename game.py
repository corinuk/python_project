import pygame
import random
SCREEN_WIDTH = 26*26
SCREEN_HEIGHT  = 32*26
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame test")

clock = pygame.time.Clock()
mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()
player = pygame.image.load("Player.png")
player = pygame.transform.scale(player, (SCREEN_WIDTH//52, SCREEN_WIDTH//52))
tower1 = pygame.image.load("test.png")
tower1 = pygame.transform.scale(tower1, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
one_pair = pygame.image.load("one_pair.png")
one_pair = pygame.transform.scale(one_pair, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
two_pair = pygame.image.load("two_pair.png")
two_pair = pygame.transform.scale(two_pair, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
triple = pygame.image.load("triple.png")
triple = pygame.transform.scale(triple, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
full_house = pygame.image.load("full_house.png")
full_house = pygame.transform.scale(full_house, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
back_straight = pygame.image.load("back_straight.png")
back_straight = pygame.transform.scale(back_straight, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
straight = pygame.image.load("straight.png")
straight = pygame.transform.scale(straight, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
mountain = pygame.image.load("mountain.png")
mountain = pygame.transform.scale(mountain, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
building_complete = pygame.image.load("building_complete.png")
building_complete = pygame.transform.scale(building_complete, (63, 38))
card_back = pygame.image.load("card_back.png")
card_back = pygame.transform.scale(card_back, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_A = pygame.image.load("spade_A.png")
spade_A = pygame.transform.scale(spade_A, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_7 = pygame.image.load("spade_7.png")
spade_7 = pygame.transform.scale(spade_7, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_8 = pygame.image.load("spade_8.png")
spade_8 = pygame.transform.scale(spade_8, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_9 = pygame.image.load("spade_9.png")
spade_9 = pygame.transform.scale(spade_9, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_10 = pygame.image.load("spade_10.png")
spade_10 = pygame.transform.scale(spade_10, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_J = pygame.image.load("spade_J.png")
spade_J = pygame.transform.scale(spade_J, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_Q = pygame.image.load("spade_Q.png")
spade_Q = pygame.transform.scale(spade_Q, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
spade_K = pygame.image.load("spade_K.png")
spade_K = pygame.transform.scale(spade_K, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_A = pygame.image.load("diamond_A.png")
diamond_A = pygame.transform.scale(diamond_A, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_7 = pygame.image.load("diamond_7.png")
diamond_7 = pygame.transform.scale(diamond_7, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_8 = pygame.image.load("diamond_8.png")
diamond_8 = pygame.transform.scale(diamond_8, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_9 = pygame.image.load("diamond_9.png")
diamond_9 = pygame.transform.scale(diamond_9, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_10 = pygame.image.load("diamond_10.png")
diamond_10 = pygame.transform.scale(diamond_10, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_J = pygame.image.load("diamond_J.png")
diamond_J = pygame.transform.scale(diamond_J, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_Q = pygame.image.load("diamond_Q.png")
diamond_Q = pygame.transform.scale(diamond_Q, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
diamond_K = pygame.image.load("diamond_K.png")
diamond_K = pygame.transform.scale(diamond_K, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_A = pygame.image.load("heart_A.png")
heart_A = pygame.transform.scale(heart_A, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_7 = pygame.image.load("heart_7.png")
heart_7 = pygame.transform.scale(heart_7, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_8 = pygame.image.load("heart_8.png")
heart_8 = pygame.transform.scale(heart_8, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_9 = pygame.image.load("heart_9.png")
heart_9 = pygame.transform.scale(heart_9, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_10 = pygame.image.load("heart_10.png")
heart_10 = pygame.transform.scale(heart_10, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_J = pygame.image.load("heart_J.png")
heart_J = pygame.transform.scale(heart_J, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_Q = pygame.image.load("heart_Q.png")
heart_Q = pygame.transform.scale(heart_Q, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
heart_K = pygame.image.load("heart_K.png")
heart_K = pygame.transform.scale(heart_K, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_A = pygame.image.load("clover_A.png")
clover_A = pygame.transform.scale(clover_A, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_7 = pygame.image.load("clover_7.png")
clover_7 = pygame.transform.scale(clover_7, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_8 = pygame.image.load("clover_8.png")
clover_8 = pygame.transform.scale(clover_8, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_9 = pygame.image.load("clover_9.png")
clover_9 = pygame.transform.scale(clover_9, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_10 = pygame.image.load("clover_10.png")
clover_10 = pygame.transform.scale(clover_10, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_J = pygame.image.load("clover_J.png")
clover_J = pygame.transform.scale(clover_J, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_Q = pygame.image.load("clover_Q.png")
clover_Q = pygame.transform.scale(clover_Q, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
clover_K = pygame.image.load("clover_K.png")
clover_K = pygame.transform.scale(clover_K, (2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13))
road1 = pygame.image.load("road.png")
road1 = pygame.transform.scale(road1, (SCREEN_WIDTH//26, SCREEN_WIDTH//26))
card_img=[[spade_A,spade_7,spade_8,spade_9,spade_10,spade_J,spade_Q,spade_K],
          [diamond_A,diamond_7,diamond_8,diamond_9,diamond_10,diamond_J,diamond_Q,diamond_K],
          [heart_A,heart_7,heart_8,heart_9,heart_10,heart_J,heart_Q,heart_K],
          [clover_A,clover_7,clover_8,clover_9,clover_10,clover_J,clover_Q,clover_K]]
player_Rect = player.get_rect()
player_Rect2 = player.get_rect()
player_Rect.centerx = SCREEN_WIDTH//26*10-1
player_Rect.centery = 0

playing = True
road=[]
tower=[]
built_tower=[]
for i in range(26):
    for j in range(25):
        if (i==2 and (j not in [0,1,13,14,23,24])):
            road.append([i,j])
        elif ((i==11 or i==14) and (j not in [0,1,23,24])):
            road.append([i,j])
        elif (i==23 and (j not in [0,1,10,11,13,14,23,24])):
            road.append([i,j])
        elif (j in [2,22] and i not in [0,1,12,13,24,25]):
            road.append([i,j])
        elif (j==15 and i not in [0,1,24,25]):
            road.append([i,j])
        elif (j==9 and i not in [24,25]):
            road.append([i,j])
        elif (j==12 and i not in [0,1]):
            road.append([i,j])
        else:
            tower.append([i,j])
a=0
health=10
step=0
tower_selected=0
poker_rand=[0,0,0,0,0]
poker_card=[[0,0] for i in range(5)]
changed=[0 for i in range(5)]
while playing:
    SCREEN.fill((0, 0, 0))
    myFont = pygame.font.SysFont( "arial", 18, True, False)
    text_Title= myFont.render("Life :"+str(health), True, 'RED')
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = 40
    text_Rect.y = 0
    SCREEN.blit(text_Title, text_Rect)
    SCREEN.blit(building_complete, (613,0))
    for i,j in road:
        SCREEN.blit(road1, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and (step==0 or step==1):
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            for i,j in tower:
                if 26*j+13<=mouse_pos[0]<=26*j+39 and 26*i+13<=mouse_pos[1]<=26*i+39:
                    if step==1:
                        built_tower.pop()
                    built_tower.append([i,j,0])
                    tower_selected=[i,j]
                    step=1
                    break
        if event.type == pygame.KEYDOWN and step==1:
            tower.remove(tower_selected)
            step=2
        if step==2:
            poker_rand=[random.randint(0,31) for i in range(5)]
            step=3
            for i in range(5):
                if 0<=poker_rand[i]<=7:
                    poker_card[i][0]=0 #spade
                elif 8<=poker_rand[i]<=15:
                    poker_card[i][0]=1 # heart
                elif 16<=poker_rand[i]<=23:
                    poker_card[i][0]=2
                elif 24<=poker_rand[i]<=34:
                    poker_card[i][0]=3
                poker_card[i][1]=poker_rand[i]%8
        if event.type == pygame.MOUSEBUTTONDOWN and step==3:
            mouse_pos = pygame.mouse.get_pos()
            if 0<=mouse_pos[0]<=104 and 702<=mouse_pos[1]<=808 and changed[0]==0:
                changed[0]=1
                poker_rand[0]=random.randint(0,31)
                if 0<=poker_rand[0]<=7:
                    poker_card[0][0]=0
                elif 8<=poker_rand[0]<=15:
                    poker_card[0][0]=1
                elif 16<=poker_rand[0]<=23:
                    poker_card[0][0]=2
                elif 24<=poker_rand[0]<=34:
                    poker_card[0][0]=3
                poker_card[0][1]=poker_rand[0]%8
            if 134<=mouse_pos[0]<=238 and 702<=mouse_pos[1]<=808 and changed[1]==0:
                changed[1]=1
                poker_rand[1]=random.randint(0,31)
                if 0<=poker_rand[1]<=7:
                    poker_card[1][0]=0
                elif 8<=poker_rand[1]<=15:
                    poker_card[1][0]=1
                elif 16<=poker_rand[1]<=23:
                    poker_card[1][0]=2
                elif 24<=poker_rand[1]<=34:
                    poker_card[1][0]=3
                poker_card[1][1]=poker_rand[1]%8
            if 268<=mouse_pos[0]<=374 and 702<=mouse_pos[1]<=808 and changed[2]==0:
                changed[2]=1
                poker_rand[2]=random.randint(0,31)
                if 0<=poker_rand[2]<=7:
                    poker_card[2][0]=0
                elif 8<=poker_rand[2]<=15:
                    poker_card[2][0]=1
                elif 16<=poker_rand[2]<=23:
                    poker_card[2][0]=2
                elif 24<=poker_rand[2]<=34:
                    poker_card[2][0]=3
                poker_card[2][1]=poker_rand[2]%8
            if 404<=mouse_pos[0]<=508 and 702<=mouse_pos[1]<=808 and changed[3]==0:
                changed[3]=1
                poker_rand[3]=random.randint(0,31)
                if 0<=poker_rand[3]<=7:
                    poker_card[3][0]=0
                elif 8<=poker_rand[3]<=15:
                    poker_card[3][0]=1
                elif 16<=poker_rand[3]<=23:
                    poker_card[3][0]=2
                elif 24<=poker_rand[3]<=34:
                    poker_card[3][0]=3
                poker_card[3][1]=poker_rand[3]%8
            if 538<=mouse_pos[0]<=642 and 702<=mouse_pos[1]<=808 and changed[4]==0:
                changed[4]=1
                poker_rand[4]=random.randint(0,31)
                if 0<=poker_rand[4]<=7:
                    poker_card[4][0]=0
                elif 8<=poker_rand[4]<=15:
                    poker_card[4][0]=1
                elif 16<=poker_rand[4]<=23:
                    poker_card[4][0]=2
                elif 24<=poker_rand[4]<=34:
                    poker_card[4][0]=3
                poker_card[4][1]=poker_rand[4]%8
        if event.type == pygame.MOUSEBUTTONDOWN and step==3:
            mouse_pos = pygame.mouse.get_pos()
            if 613<=mouse_pos[0] and 0<=mouse_pos[1]<=38:
                sorted_poker_card=sorted(poker_card,key=lambda x: x[1])
                if poker_card[0]==poker_card[1]==poker_card[2]==poker_card[3]==poker_card[4]: #파이브카드 플러시
                    built_tower[-1][2]=0
                elif poker_card[0][1]==poker_card[1][1]==poker_card[2][1]==poker_card[3][1]==poker_card[4][1]: #파이브카드
                    built_tower[-1][2]=1
                elif sorted_poker_card[0][1]==sorted_poker_card[1][1]==sorted_poker_card[2][1]==sorted_poker_card[3][1] or sorted_poker_card[1][1]==sorted_poker_card[2][1]==sorted_poker_card[3][1]==poker_card[4][1]: #포카드
                    built_tower[-1][2]=2
                elif (poker_card[0][0]==poker_card[1][0]==poker_card[2][0]==poker_card[3][0]==poker_card[4][0]) and sorted([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]])==[0,4,5,6,7]: #로얄 스트레이트 플러시
                    built_tower[-1][2]=3
                elif (poker_card[0][0]==poker_card[1][0]==poker_card[2][0]==poker_card[3][0]==poker_card[4][0]) and sorted([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]])==[0,1,2,3,4]: #백 스트레이트 플러시
                    built_tower[-1][2]=4
                elif (poker_card[0][0]==poker_card[1][0]==poker_card[2][0]==poker_card[3][0]==poker_card[4][0]) and sorted([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]]) in [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]: #스트레이트 플러시
                    built_tower[-1][2]=5
                elif poker_card[0][0]==poker_card[1][0]==poker_card[2][0]==poker_card[3][0]==poker_card[4][0]: #플러시
                    built_tower[-1][2]=6
                elif sorted([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]])==[0,4,5,6,7]: #마운틴
                    built_tower[-1][2]=7
                elif sorted([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]])==[0,1,2,3,4]: #백스트레이트
                    built_tower[-1][2]=8
                elif sorted([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]]) in [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]]: #스트레이트
                    built_tower[-1][2]=9
                elif len(set([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]]))==2: #풀하우스
                    built_tower[-1][2]=10
                elif sorted_poker_card[0]==sorted_poker_card[1]==sorted_poker_card[2] or sorted_poker_card[1]==sorted_poker_card[2]==sorted_poker_card[3] or sorted_poker_card[2]==sorted_poker_card[3]==sorted_poker_card[4]: #트리플
                    built_tower[-1][2]=11
                elif len(set([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]]))==3: #투페어
                    built_tower[-1][2]=12
                elif len(set([poker_card[0][1],poker_card[1][1],poker_card[2][1],poker_card[3][1],poker_card[4][1]]))==4: #원페어
                    built_tower[-1][2]=13
                else:
                    built_tower[-1][2]=14
                step=4
    for i,j,k in built_tower:
        if k==8:
            SCREEN.blit(straight, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
        elif k==9:
            SCREEN.blit(back_straight, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
        elif k==10:
            SCREEN.blit(full_house, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
        elif k==11:
            SCREEN.blit(triple, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
        elif k==12:
            SCREEN.blit(two_pair, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
        elif k==13:
            SCREEN.blit(one_pair, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
        else:
            SCREEN.blit(tower1, [SCREEN_WIDTH//26*j+13, SCREEN_WIDTH//26*i+13])
    for i in range(5):
        if step<3:
            SCREEN.blit(card_back, [SCREEN_WIDTH//5*i, SCREEN_WIDTH//26*27])
        else:
            SCREEN.blit(card_img[poker_card[i][0]][poker_card[i][1]], [SCREEN_WIDTH//5*i, SCREEN_WIDTH//26*27])
    if step==4:
        if a%4==0:
            player_Rect.y+=1
        elif a%4==1:
            player_Rect.x-=1
        elif a%4==2:
            player_Rect.y-=1
        elif a%4==3:
            player_Rect.x+=1
        if player_Rect.bottom > SCREEN_WIDTH//26*24+13 and (a==0 or a==4):
            a+=1
            player_Rect.y-=1
        elif player_Rect.left < SCREEN_WIDTH//26*2+13 and (a==1 or a==9):
            a+=1
            player_Rect.x+=1
        elif player_Rect.top < SCREEN_WIDTH//26*14+13 and a==2:
            a+=1
            player_Rect.y+=1
        elif player_Rect.right > SCREEN_WIDTH//26*23+13 and a==3:
            a+=1
            player_Rect.x-=1
        elif player_Rect.left < SCREEN_WIDTH//26*15+13 and a==5:
            a+=1
            player_Rect.y-=1
        elif player_Rect.top < SCREEN_WIDTH//26*2+13 and (a==6 or a==10):
            a+=1
            player_Rect.x+=1
        elif player_Rect.right > SCREEN_WIDTH//26*23+13 and a==7:
            a+=1
            player_Rect.y+=1
        elif player_Rect.bottom > SCREEN_WIDTH//26*12+13 and a==8:
            a+=1
            player_Rect.x-=1
        elif player_Rect.right > SCREEN_WIDTH//26*13+13 and a==11:
            a+=1
            player_Rect.y-=1
        elif player_Rect.bottom > SCREEN_WIDTH//26*26+13 and a==12:
            health-=1
            a=0.1
        SCREEN.blit(player, player_Rect)
    pygame.display.flip()
    clock.tick(120)
























































































































































































