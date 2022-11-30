def Map():
    road = []
    tower_available = []
    road.append([0,9])
    road.append([25,12])
    for i in range(1,25):
        for j in range(25):
            if (i == 2 and (j not in [0, 1, 13, 14, 23, 24])):
                road.append([i, j])
            elif ((i == 11 or i == 14) and (j not in [0, 1, 23, 24])):
                road.append([i, j])
            elif (i == 23 and (j not in [0, 1, 10, 11, 13, 14, 23, 24])):
                road.append([i, j])
            elif (j in [2, 22] and i not in [0, 1, 12, 13, 24, 25]):
                road.append([i, j])
            elif (j == 15 and i not in [0, 1, 24, 25]):
                road.append([i, j])
            elif (j == 9 and i not in [24, 25]):
                road.append([i, j])
            elif (j == 12 and i not in [0, 1]):
                road.append([i, j])
            else:
                tower_available.append([i, j])
    return road, tower_available
