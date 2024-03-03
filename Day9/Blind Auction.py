# import os
# os.system('cls')
from art import logo

# #HINT: You can call clear() to clear the output in the console.
# print(logo)
print("Welcome to the secret auction program ")


def find_highest_bidder(bidding_record):
    highest_bid = 0

    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"the winner is {winner} he won with the bid of {highest_bid}$")


bids = {}

continue_the_bid = "yes"
while continue_the_bid == "yes":
    name = input("what is your name? \n")
    bid = int(input("what is your bid in $? \n"))
    bids[name] = bid
    continue_the_bid = input("are they any other bidders? yes pr no ? ")

print(bids)
find_highest_bidder(bids)
# winner = max(bids)
# print(winner)
