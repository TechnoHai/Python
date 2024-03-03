# Calculator
from art import logo
# Add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


# a dictionary of operation symbols pointing to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


# an empty function so we can call her and run her again if the user choose no  .
def calculator():
    print(logo)

    num1 = float(input("what is the first number ? \n"))

    # printing the operations symbols
    for symbol in operations:
        print(symbol)

    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("please choose an operation \n")

        num2 = float(input("what is the next number ?\n"))

        calculation_function = operations[operation_symbol]  # calculation_function is getting the value of one of the operation answer
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculate with {answer} or 'n' to start over! ") == "y":
            num1 = answer  # num1 is getting first number answer for future calculation
        else:
            continue_calculation = False  # stop the while loop
            calculator()  # call the calculator function and start over the calculation


calculator()
