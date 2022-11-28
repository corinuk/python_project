def card_ranking(poker_card):
    sorted_poker_card = sorted(poker_card, key=lambda x: x[1])
    
    if poker_card[0] == poker_card[1] == poker_card[2] == poker_card[3] == poker_card[4]:
        Ranking = 0
        Power = 175
    elif poker_card[0][1] == poker_card[1][1] == poker_card[2][1] == poker_card[3][1] == poker_card[4][1]:
        Ranking = 1
        Power = 125
    elif sorted_poker_card[0][1] == sorted_poker_card[1][1] == sorted_poker_card[2][1] == sorted_poker_card[3][1] or sorted_poker_card[1][1] == sorted_poker_card[2][1] == sorted_poker_card[3][1] == sorted_poker_card[4][1]:
        Ranking = 2
        Power = 69
    elif (poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]) and sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 4, 5, 6, 7]:
        Ranking = 3
        Power = 195
    elif (poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]) and sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 1, 2, 3, 4]:
        Ranking = 4
        Power = 165
    elif (poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]) and sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]:
        Ranking = 5
        Power = 145
    elif poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]:
        Ranking = 6
        Power = 92
    elif sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 4, 5, 6, 7]:
        Ranking = 7
        Power = 81
    elif sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 1, 2, 3, 4]:
        Ranking = 8
        Power = 71
    elif sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]:
        Ranking = 9
        Power = 56
    elif len(set([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]])) == 2:
        Ranking = 10
        Power = 51
    elif sorted_poker_card[0][1] == sorted_poker_card[1][1] == sorted_poker_card[2][1] or sorted_poker_card[1][1] == sorted_poker_card[2][1] == sorted_poker_card[3][1] or sorted_poker_card[2][1] == sorted_poker_card[3][1] == sorted_poker_card[4][1]:
        Ranking = 11
        Power = 40
    elif len(set([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]])) == 3:
        Ranking = 12
        Power = 30
    elif len(set([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]])) == 4:
        Ranking = 13
        Power = 20
    else:
        Ranking = 14
        Power = 10
    
    return Ranking, Power
