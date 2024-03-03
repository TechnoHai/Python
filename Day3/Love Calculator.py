
# print(str.lower("HAI"))
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# str.lower part of the string objet , convert capital letters to lower case
name1 = str.lower(name1)
name2 = str.lower(name2)

sum_names = name1 + name2
# str.count() Count occurrences of a character in string

counter_true = sum_names.count('t') + sum_names.count('r') + sum_names.count('u') + sum_names.count('e')
counter_love = sum_names.count('l') + sum_names.count('o') + sum_names.count('v') + sum_names.count('e')
counter_total = int(str(counter_true) + str(counter_love))
# print(type(counter_love))
# print(type(counter_true))
# print(type(counter_total))
# print(counter_total)
if (counter_total > 90) or (counter_total < 10):
    print(f"Your score is {counter_total}, you go together like coke and mentos.")
elif 40 < counter_total < 50:
    print(f"Your score is {counter_total}, you are alright together.")
else:
    print(f"Your score is {counter_total}")
