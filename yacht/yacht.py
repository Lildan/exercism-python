# Score categories
# Change the values as you see fit
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    dice.sort()
    
    if category == YACHT:
        if dice.count(dice[0]) == len(dice):
            return 50
        else:
            return 0

    if category == ONES:
        return sum([x for x in dice if x == 1])
    if category == TWOS:
        return sum([x for x in dice if x == 2])
    if category == THREES:
        return sum([x for x in dice if x == 3])
    if category == FOURS:
        return sum([x for x in dice if x == 4])
    if category == FIVES:
        return sum([x for x in dice if x == 5])
    if category == SIXES:
        return sum([x for x in dice if x == 6])
    if category == FULL_HOUSE:
        if dice.count(dice[2]) == 3 and (dice.count(dice[0]) == 2 or dice.count(dice[4]) == 2):
            return sum(dice)
        else:
            return 0
    
    if category == FOUR_OF_A_KIND:
        if dice.count(dice[2]) >= 4:
            return 4*dice[2]
        else:
             return 0

    if category == LITTLE_STRAIGHT:
        i = 1
        for val in dice:
            if val != i:
                return 0
            i += 1
        return 30

    if category == BIG_STRAIGHT:
        i = 2
        for val in dice:
            if val != i:
                return 0
            i += 1
        return 30

    if category == CHOICE:
        return sum(dice)

    return 0

        


    
