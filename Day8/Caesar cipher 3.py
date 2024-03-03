alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_input=text, shift_input=shift):
    alphabet_shift = alphabet * 2  # in order to avoid index error we multiply the alphabet
    encrypt_text = ""
    for letter in text_input:
        position_in_alphabet = alphabet.index(letter)  # find the letter position in the alphabet
        encrypt_text += alphabet_shift[position_in_alphabet + shift_input]  # shift the letter
    print(f"The encoded text is : {encrypt_text}")


def decrypt(text_input=text, shift_input=shift):
    decrypt_text = ""
    for letter in text_input:
        position_in_alphabet = alphabet.index(letter)  # find the letter position in the alphabet
        decrypt_text += alphabet[position_in_alphabet - shift_input]  # shift the letter
    print(f"The coded text is : {decrypt_text}")


def caesar(input_direction = direction, text_input=text, shift_input=shift):
    encrypt_text = ""
    decrypt_text = ""
    output_text = ""
    for letter in text_input:
        position_in_alphabet = alphabet.index(letter)  # find the letter position in the alphabet
        if direction == "encode":
            output_text += alphabet[position_in_alphabet + shift_input]  # shift the letter

        elif direction == "decode":
            output_text += alphabet[position_in_alphabet - shift_input]  # shift the letter
    print(f"your {direction} text is: {output_text}")



caesar(input_direction=direction, text_input=text, shift_input=shift)
