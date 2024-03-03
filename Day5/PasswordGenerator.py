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
password_length = nr_letters + nr_symbols + nr_letters

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# output_xxxx random the first letter/symbol/number
output_letter = letters[random.randint(1, nr_letters)]
output_symbol = symbols[random.randint(1, nr_symbols)]
output_number = numbers[random.randint(1, nr_numbers)]

# for look in the range of the input from the user
# its using the random.randint to generate a random number for the letter list
for letter in range(1, nr_letters):
    random_position = random.randint(1, nr_letters)
    output_letter += letters[random_position]

for symbol in range(1, nr_symbols):
    random_position = random.randint(1, nr_symbols)
    output_symbol += symbols[random_position]

for number in range(1, nr_numbers):
    random_position = random.randint(1, nr_symbols)
    output_number += numbers[random_position]

# print(output_letter)
# print(output_symbol)
# print(output_number)

easy_password = output_letter + output_symbol + output_number
print(f"your password in easy mode is {easy_password}")
#converte easy password to a list
list_easy_password = list(easy_password)
#make easy password list random
random.shuffle(list_easy_password)
#combine easy password list to a string
easy_password = ''.join(list_easy_password)
print(f"your password in hard mode is {easy_password}")


# input_easy_password = list(easy_password)
# print(input_easy_password)
# hard_password = random.shuffle(input_easy_password)
# print(hard_password)

# hard_password = input_easy_password[random.randint(1, password_length-1)]
#
# for carecter in range(1, password_length  ):
#     random_position = random.randint(1, password_length)
#     hard_password += input_easy_password[random_position-1]
#
# print(f"your password in hard mode is {hard_password}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
