# The Modulo Operator
# Often you'll want to know what is the
# remainder after a division.
# e.g. 4 ÷ 2 = 2 with no remainder
# but 5 ÷ 2 = 2 with 1 remainder
# The modulo does not give you the result
# of the division, just the remainder.
# It can be really helpful in certain situations,
# e.g. figuring out if a number is odd or even.

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_modulo = number % 2

if (number % 2) > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
