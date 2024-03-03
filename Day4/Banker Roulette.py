

# 🚨 Don't change the code below 👇
import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#len count the number of object in the list names
names_count = len(names)
#generating a random number between 0 to the names_count value

random_number = random.randint(0, names_count - 1 )
print(random_number)

#random.choice Return a random element from the list
payer_choice = random.choice(names)

#print the name in the list accordind to the random number
print(f"and the lucky basterd is: {names[random_number]}")
print(f"now we are using the choice option:  {payer_choice}")
