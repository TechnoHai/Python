import random
import os


import os
def clear():
    os.system('cls')  # on Windows System


# the deck of cards for balck jack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# random_card = random.choice(cards)
# user_hand = []
# computer_cards = []
# cards_number = 2


# print(random_card)
def deal_card():
    """choose random card from the deck"""
    # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(sum_cards):
    """calculate the sum of the user/computer cards ."""
    total = 0
    # if total > 21:
    #     for val in sum_cards:
    #         if val == 11:
    #             total = total - 10
    if 11 in sum_cards and total > 21:
        sum_cards.remove(11)
        sum_cards.append(1)
    total = sum(sum_cards)

    return total


def compere(user_score, computer_score):
    """ compere the computer and user sums and decide who won """
    if user_score > 21:
        print(f"dealer win user:{user_score} dealer: {computer_score}")
    elif computer_score > 21:
        print(f"user win user:{user_score} dealer: {computer_score}")
    elif user_score == computer_score:
        print(f"its a draw user:{user_score} dealer: {computer_score}")
    elif user_score == 21:
        print(f"user Win user:{user_score} dealer: {computer_score}")
    elif user_score > computer_score:
        print(f"user win user:{user_score} dealer: {computer_score}")
    else:
        print(f"dealer win user:{user_score} dealer: {computer_score}")


def blackjack():
    # play_balckjack = input("do you want to play blackjack? ") =="y"
    user_cards = []
    computer_cards = []
    continue_game = True
    # deal 2 cards for the computer and users ,
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    print(f"Your cards :{user_cards}, current score : {user_score}")
    print(f"Computer first card : {computer_cards[0]}")

    # check if computer got blackjack on the first try
    if computer_score == 21 and user_score == 21 and user_score > 21:
        print("the house wins")
        continue_game = False

    # user side if hw choose to draw another card
    continue_game = True
    while continue_game:
        get_another_card = input("type 'y' to get another card type 'n' to pass ")
        if get_another_card == "y":

            user_cards.append(deal_card())
            # user_hand = user_cards
            user_score = calculate_score(user_cards)

            print(user_cards)

            print(calculate_score(user_cards))

            if calculate_score(user_cards) > 21:
                continue_game = False
        else:
            continue_game = False

    # computer side of the game
    while computer_score < 17:
        if computer_score < user_score:
            computer_cards.append(deal_card())
            # computer_cards = computer_cards
            computer_score = calculate_score(computer_cards)

            print(f"this is the dealer cards {computer_cards} dealer card sum : {computer_score} ")
        else:
            continue_game = False
    compere(user_score, computer_score)
    another_game = input("do you want to play another game ? 'y' or 'n'")
    if another_game == "y":
        os.system('cls')
        blackjack()


blackjack()
