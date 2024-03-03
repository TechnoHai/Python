#simple function
def greet():
    print("hello once")
    print("hello twice")
    print("hello there")


# greet()


# function with input
# def greet_with_name(name):
#     print(f"hello {name} ")


# greet_with_name("hai")

def greet_with_name_location(name, location):
    print(f"hello {name} ")
    print(f"how is the life in {location}")


greet_with_name_location(location="tel-aviv", name="hai")
