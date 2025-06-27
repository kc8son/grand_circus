####################################################################################################
#
#   Date Written: 03/27/2023        By: Joseph P. Merten
#   Day 14: Poker-Spades Game - Unit Testing Practice
#
####################################################################################################
#   imports
import pdb
import sys
import math

####################################################################################################
#   Variables
cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

####################################################################################################
#   Functions
def lets_play_cards():
    # print(check_straight("s3", "s2", "s1"))
    # print(check_straight("sa", "sk", "sq"))
    # print(check_straight("s10", "sj", "sq"))

    # print(check_3ofa_kind("s5", "s5", "s5"))
    # print(check_3ofa_kind("sq", "sq", "sq"))
    # print(check_3ofa_kind("sa", "sa", "sa"))
    # print(check_3ofa_kind("sa", "sq", "sq"))
    # print(check_3ofa_kind("sq", "sq", "sa"))

    # print(check_royal_flush("sa", "sq", "sk"))
    # print(check_royal_flush("sq", "sq", "sa"))
    # print(check_royal_flush("sq", "sk", "sj"))

    # print(play_cards("sa", "sq", "sk", "sq", "sk", "sj")) # test straights
    # print(play_cards("sq", "sk", "sj", "sa", "sq", "sk"))
    # print(play_cards("sa", "sq", "sk", "sa", "sq", "sk"))
    #
    # print(play_cards("sa", "sq", "sk", "s5", "s5", "s5")) # Test 3 of a kind
    # print(play_cards("s5", "s5", "s5", "sa", "sq", "sk"))
    # print(play_cards("s5", "s5", "s5", "s5", "s5", "s5"))
    #
    # print(play_cards("s3", "s2", "s1", "s10", "sj", "sq")) # straight
    # print(play_cards("s10", "sj", "sq", "s3", "s2", "s1"))
    # print(play_cards("s3", "s2", "s1", "s3", "s2", "s1"))

    print("--- Nothing to do here - it's all esting")


def get_rank(card):
    """This function gets the rank value of the card passed."""
    card = card.lower()
    if card[1:] in "jqka".lower():
        match card[1:]:
            case "j":
                card_val = 11
            case "q":
                card_val = 12
            case "k":
                card_val = 13
            case "a":
                card_val = 14
    elif card[1:] in "2345678910":
        card_val = int(card[1:])
    else:
        card_val = 0
    # print(card , card_val)
    return card_val
def check_straight(card1, card2, card3):
    """If the cards passed in are three cards in a sequence, this function returns the greatest value.
    Otherwise it returns 0. For example, check_straight('S5','S6','S7') would return 7. check_straight('S6', 'S5', 'S7')
    would also return 7.  check_straight('S3','SQ','SK') would return 0. Come up with several tests."""
    my_cards = []
    my_cards.append(get_rank(card1))
    my_cards.append(get_rank(card2))
    my_cards.append(get_rank(card3))
    my_cards.sort()
    if my_cards[2] - my_cards[1] == 1 and my_cards[1] - my_cards[0] == 1:
        return my_cards[2]
    else:
        return 0
def check_3ofa_kind(card1, card2, card3):
    """If the three cards passed in are all the same, return the value. Otherwise return 0. For example,
    check_3ofa_kind('S9', 'S9', 'S9') would return 9. check_3ofa_kind('S2', 'S4', 'S2') would return 0."""
    if get_rank(card1) == get_rank(card2) and get_rank(card2) == get_rank(card3):
        return get_rank(card2)
    else:
        return 0
def check_royal_flush(card1, card2, card3):
    """(The code in this function will make use of the check_straight function from earlier, and will assume
    it’s been tested already and is functioning correctly.) If the cards passed in are a straight with the value of 14,
    then this function returns 14. Otherwise it returns 0. For this one, you only need maybe three tests."""
    if check_straight(card1, card2, card3) == 14:
        return check_straight(card1, card2, card3)
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    """This method takes three cards for the left player (left1, left2, left3) and three cards for the right
    player (right1, right2, right3) and determines who wins.
        If left wins, it returns -1.
        If neither win (a draw), it returns 0.
        If right wins, it returns 1.
        """
    left_scores = [
        check_3ofa_kind(left1, left2, left3),
        check_straight(left1, left2, left3),
        check_royal_flush(left1, left2, left3)
    ]
    right_scores = [
        check_3ofa_kind(right1, right2, right3),
        check_straight(right1, right2, right3),
        check_royal_flush(right1, right2, right3)
    ]
    # print(left_scores)
    # print(right_scores)
    # mleft = max(left_scores)
    # mright = max(right_scores)
    # print(f"Left: {mleft}\tRight: {mright}")
    if max(left_scores) > max(right_scores):
        return -1
    elif max(left_scores) < max(right_scores):
        return 1
    else:
        return 0


####################################################################################################
#   Classes

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
if __name__ == '__main__':
    lets_play_cards()
