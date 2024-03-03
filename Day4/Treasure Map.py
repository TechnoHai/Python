# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# [['a⬜️', 'b⬜️', 'c⬜️'], ['d⬜️', 'e⬜️', 'f⬜️'], ['g⬜️', 'h⬜️', 'i⬜️']]

#Write your code below this row 👇

# list(str(12345))


# position_list = list(str(position))
column = int(position[0]) - 1
row = int(position[1]) - 1
# print(map[column][row])

map[column][row] = 'X'
if map ==






#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}\n")
# print(map)
