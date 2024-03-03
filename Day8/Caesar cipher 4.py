# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2


def caesar(input_direction, text_input, shift_input):
    output_text = ""
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    caesar_alphabet = alphabet
    if shift_input > 22:
        caesar_alphabet = caesar_alphabet * 2

    for letter in text_input:

        if input_direction == "encode":
            if letter in alphabet:
                position_in_alphabet = caesar_alphabet.index(letter)  # find the letter position in the alphabet
                output_text += caesar_alphabet[position_in_alphabet + shift_input]  # shift the letter

            else:
                output_text += str(letter)

        elif input_direction == "decode":
            # TODO-3: What happens if the user enters a number/symbol/space?
            # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            if letter in alphabet:  # if a letter is not in the list we converting it to string and adding it to output file
                position_in_alphabet = caesar_alphabet.index(letter)  # find the letter position in the alphabet
                output_text += caesar_alphabet[position_in_alphabet - shift_input]  # shift the letter
            else:  # if a letter is not in the list we converting it to string and adding it to output file
                output_text += str(letter)
    print(f"your {direction} text is: {output_text}")


print(logo)
continue_input = "yes"
while continue_input == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(input_direction=direction, text_input=text, shift_input=shift)
    continue_input = input("do tou want yo play again? yes or no? \n")
