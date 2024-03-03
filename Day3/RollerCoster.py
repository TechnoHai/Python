height = int(input("what is your height? "))
bill = 0

if height > 120:
    print("you can ride the train!")
    age = int(input("how old are you? "))
    if 45 <= age <= 55:
        bill = 0
    elif age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    elif age > 18:
        bill = 12
    photo = input("would you like some photo? yes or no ")
    if photo == 'no' or (45 <= age <= 55):
        print(f"your bill is {bill}$:")
    else:
        print("your bill is $:", bill + 3)


else:
    print("you are too short sorry ")
