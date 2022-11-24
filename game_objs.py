import pygame

SCREEN_WIDTH = 26*26
SCREEN_HEIGHT = 32*26
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Objects:
    def __init__(self, img, width, height):
        self.width = SCREEN_WIDTH//26
        self.height = SCREEN_HEIGHT//26
        self.img_load = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img_load, (width, height))

    def show(self, x, y):
        SCREEN.blit(self.img, [x, y])
    
    def rect(self):
        rect = self.img.get_rect()
        rect.centerx = SCREEN_WIDTH//26*10-1
        rect.centery = 0
        return rect

def Rankings():
    five_card_flush = Objects("./towers/five_card_flush.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    five_card = Objects("./towers/five_card.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    four_card = Objects("./towers/four_card.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    royal_straight_flush = Objects("./towers/royal_straight_flush.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    back_straight_flush = Objects("./towers/back_straight_flush.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    straight_flush = Objects("./towers/straight_flush.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    flush = Objects("./towers/flush.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    mountain = Objects("./towers/mountain.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    back_straight = Objects("./towers/back_straight.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    straight = Objects("./towers/straight.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    full_house = Objects("./towers/full_house.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    triple = Objects("./towers/triple.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    two_pair = Objects("./towers/two_pair.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    one_pair = Objects("./towers/one_pair.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    top = Objects("./towers/top.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    tower1 = Objects("./towers/test.png", SCREEN_WIDTH//26, SCREEN_HEIGHT//26)
    Rankings = [five_card_flush, five_card, four_card, royal_straight_flush, back_straight_flush,
            straight_flush, flush, mountain, back_straight, straight, full_house, triple, two_pair, one_pair, top]
    return Rankings, tower1

def Cards():
    spade_A = Objects("./cards/spade_A.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_7 = Objects("./cards/spade_7.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_8 = Objects("./cards/spade_8.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_9 = Objects("./cards/spade_9.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_10 = Objects("./cards/spade_10.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_J = Objects("./cards/spade_J.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_Q = Objects("./cards/spade_Q.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade_K = Objects("./cards/spade_K.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_A = Objects("./cards/diamond_A.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_7 = Objects("./cards/diamond_7.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_8 = Objects("./cards/diamond_8.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_9 = Objects("./cards/diamond_9.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_10 = Objects("./cards/diamond_10.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_J = Objects("./cards/diamond_J.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_Q = Objects("./cards/diamond_Q.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    diamond_K = Objects("./cards/diamond_K.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_A = Objects("./cards/heart_A.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_7 = Objects("./cards/heart_7.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_8 = Objects("./cards/heart_8.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_9 = Objects("./cards/heart_9.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_10 = Objects("./cards/heart_10.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_J = Objects("./cards/heart_J.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_Q = Objects("./cards/heart_Q.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    heart_K = Objects("./cards/heart_K.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_A = Objects("./cards/clover_A.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_7 = Objects("./cards/clover_7.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_8 = Objects("./cards/clover_8.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_9 = Objects("./cards/clover_9.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_10 = Objects("./cards/clover_10.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_J = Objects("./cards/clover_J.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_Q = Objects("./cards/clover_Q.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    clover_K = Objects("./cards/clover_K.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    card_back = Objects("./cards/card_back.png", 2*SCREEN_WIDTH//13, 2*SCREEN_WIDTH//13)
    spade = [spade_A, spade_7, spade_8, spade_9, spade_10, spade_J, spade_Q, spade_K]
    diamond = [diamond_A, diamond_7, diamond_8, diamond_9, diamond_10, diamond_J, diamond_Q, diamond_K]
    heart = [heart_A, heart_7, heart_8, heart_9, heart_10, heart_J, heart_Q, heart_K]
    clover = [clover_A, clover_7, clover_8, clover_9, clover_10, clover_J, clover_Q, clover_K]
    card_img = [spade, diamond, heart, clover]
    return card_img, card_back

def Building_complete():
    building_complete = Objects("building_complete.png", 63, 38)
    return building_complete

def Road():
    road1 = Objects("road.png", SCREEN_WIDTH//26, SCREEN_WIDTH//26)
    return road1

def Player():
    player = Objects("Player.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return player

def red_Ball():
    red_ball = Objects("red.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return red_ball

def blue_Ball():
    blue_ball = Objects("blue.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return blue_ball

def exp_1():
    exp_1 = Objects("exp_1.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return exp_1

def exp_2():
    exp_2 = Objects("exp_2.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return exp_2

def exp_3():
    exp_3 = Objects("exp_3.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return exp_3

def exp_4():
    exp_4 = Objects("exp_4.png", SCREEN_WIDTH//52, SCREEN_WIDTH//52)
    return exp_4