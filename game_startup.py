def Startup_setting(player):
    step = 0
    unit_count = 0
    unit=[]
    poker_rand = [0, 0, 0, 0, 0]
    poker_card = [[0, 0] for i in range(5)]
    changed = [0 for i in range(5)]
    player_Rect = [player.rect() for i in range(15)]
    return step, unit_count, unit, poker_rand, poker_card, changed, player_Rect