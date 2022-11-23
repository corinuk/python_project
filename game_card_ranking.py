def card_ranking(poker_card):
    sorted_poker_card = sorted(poker_card, key=lambda x: x[1])
    
    five_card_flush_ = poker_card[0] == poker_card[1] == poker_card[2] == poker_card[3] == poker_card[4]
    
    five_card_ = poker_card[0][1] == poker_card[1][1] == poker_card[2][1] == poker_card[3][1] == poker_card[4][1]
    
    four_card_ = sorted_poker_card[0][1] == sorted_poker_card[1][1] == sorted_poker_card[2][1] == sorted_poker_card[
        3][1] or sorted_poker_card[1][1] == sorted_poker_card[2][1] == sorted_poker_card[3][1] == poker_card[4][1]
    
    royal_straight_flush_ = (poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]) and sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 4, 5, 6, 7]
    
    back_straight_flush_ = (poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]) and sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 1, 2, 3, 4]
    
    straight_flush_ = (poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]) and sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
    
    flush_ = poker_card[0][0] == poker_card[1][0] == poker_card[2][0] == poker_card[3][0] == poker_card[4][0]
    
    mountain_ = sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 4, 5, 6, 7]
    
    back_straight_ = sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) == [0, 1, 2, 3, 4]
    
    straight_ = sorted([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]]) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
    
    full_house_ = len(set([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]])) == 2
    
    triple_ = sorted_poker_card[0][1] == sorted_poker_card[1][1] == sorted_poker_card[2][1] or sorted_poker_card[1][1] == sorted_poker_card[2][1] == sorted_poker_card[3][1] or sorted_poker_card[2][1] == sorted_poker_card[3][1] == sorted_poker_card[4][1]
    
    two_pair_ = not triple_ and len(set([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]])) == 3
    
    one_pair_ = len(set([poker_card[0][1], poker_card[1][1], poker_card[2][1], poker_card[3][1], poker_card[4][1]])) == 4
    
    Rankings = [five_card_flush_, five_card_, four_card_, royal_straight_flush_, back_straight_flush_,
                straight_flush_, flush_, mountain_, back_straight_, straight_, full_house_, triple_, two_pair_, one_pair_]
    return Rankings
