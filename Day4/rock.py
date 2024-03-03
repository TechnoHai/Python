# Rock Paper Scissors
# Instructions
# Make a rock, paper, scissors game.
#
# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
#
# Start the game by asking the player:
#
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#
# From there you will need to figure out:
#
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#geting a number between 0-2 from the user and converting it to int
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#בניתי טבלה על נייר משתמש/מחשב והשוואתי תוצאות לפי המשתמש
raw1 = ['even', 'computer', 'user']
raw2 = ['user', 'even', 'computer']
raw3 = ['computer', 'user', 'even']


outcome = [raw1, raw2, raw3]


#creating a random number for the  computer .

computer = random.randint(0, 2)

# print(user)
# print(computer)
#
# print(outcome[user][computer])

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

print("computer choose: ")

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

print(f"and the result is {outcome[user][computer]} WINSSSS!!!!")













