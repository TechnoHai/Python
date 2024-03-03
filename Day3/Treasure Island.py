print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision_1 = input('you are in the dark forest, you arrived to a crossword . where do you want to go? "left" or "right" ? ').lower()
# decision_2 = 0
# decision_3 = 0
# decision_4 = 0

if decision_1 == 'left':
    decision_2 = input('you arrived to the river , "wait" for the boat man or "swim" to the other side? ')

    if decision_2 == 'wait':
        decision_3 = input('you arrived to to the castle , at the end of the corridor there are two doors , choose "red" or "blue" ')

        if decision_3 == 'yellow':
            print("YOU WIN!!!!")
        elif decision_3 == 'red':
            print("Burned by fire! \n YOU DIED!")
        elif decision_3 == 'blue':
            print("Eaten by beasts \n YOU DIED!!")
        else:
            print("GAME OVER!")

    else:
        print("Attacked by a shark ! \n YOU DIED!")
else:
    print("Fall into a hole \n YOU DIED!  ")


#decision_2 = input("you arrived to the river , wait for the boat man or swim to the other side? ")



# decision_2 = input()
# print(decision_2)
#print("you fell into the abyss!\nYOU DIED!!!")


