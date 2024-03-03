import random

# the deck of cards for balck jack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# random_card = random.choice(cards)
user_hand = []
dealer_hand = []
cards_number = 2


# print(random_card)
def dealer(n):
    hand = []

    for i in range(n):
        hand.append((random.choice(cards)))
    return hand


def calculate_score(list):
    total = sum(list)
    if total > 21:
        for val in list:
            if val == 11:
                total = total - 10

    return total

def compere(sum1, sum2):
    if sum1 > 21:
        print("dealer win")
    elif sum2 > 21:
        print("user win")
    elif sum1 == sum2:
        print(f"its a draw user:{sum1} dealer: {sum2}")
    elif sum1 == 21:
        print("you Win")
    elif sum1 > sum2:
        print("the user won")
    else:
        print(f"the house win {sum2}")


# play_balckjack = input("do you want to play blackjack? ") =="y"
user_first_hand = dealer(2)
dealer_first_hand = dealer(2)
dealer_hand_sum = calculate_score(dealer_first_hand)
user_hand_sum = calculate_score(user_first_hand)
print(f"Your cards :{user_first_hand}, current score : {user_hand_sum}")
print(f"Computer first card : {dealer_first_hand[0]}")

if dealer_hand_sum == 21 and user_hand_sum == 21:
    print("the house wins")
elif dealer_hand_sum == 21:
    print("the house wins")
elif user_hand_sum == 21:
    print("you Win")

# user side if hw choose to draw another card
continue_game = True
while continue_game:
    get_another_card = input("type 'y' to get another card type 'n' to pass ")
    if get_another_card == "y":
        new_card = dealer(1)
        user_first_hand.append(new_card[0])
        user_hand = user_first_hand
        user_hand_sum = calculate_score(user_hand)

        print(user_hand)

        print(calculate_score(user_hand))

        if calculate_score(user_hand) > 21:
            continue_game = False
    else:
        continue_game = False

# computer side of the game
while dealer_hand_sum < 17:
    if dealer_hand_sum < user_hand_sum:
        new_card = dealer(1)
        dealer_first_hand.append(new_card[0])
        dealer_hand = dealer_first_hand
        dealer_hand_sum = calculate_score(dealer_hand)

        print(f"this is the dealer hand {dealer_hand} dealer sum : {dealer_hand_sum} ")

compere(user_hand_sum, dealer_hand_sum)

# if user_hand_sum > 21:
#     print("dealer win")
# elif dealer_hand_sum > 21:
#     print("user win")
# elif user_hand_sum == dealer_hand_sum:
#     print(f"its a draw user:{user_hand_sum} dealer: {dealer_hand_sum}")
# elif user_hand_sum == 21:
#     print("you Win")
# elif user_hand_sum > dealer_hand_sum:
#     print("the user won")
# else:
#     print(f"the house win {dealer_hand_sum}")
