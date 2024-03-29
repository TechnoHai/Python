import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# empty string


# for look in the range of the input from the user
# it's using the random.randint to generate a random number for the letter list
easy_password = ""

for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    easy_password += random_letter

for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    easy_password += random_symbol

for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    easy_password += random_number

print(easy_password)

# easy_password = output_letter + output_symbol + output_number
# print(easy_password)
# convert easy password to a list
easy_password_list = list(easy_password)
random.shuffle(easy_password_list)
# combine easy password to a string
hard_password = ''.join(easy_password_list)
print(hard_password)
