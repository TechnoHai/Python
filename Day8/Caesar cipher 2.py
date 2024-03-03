alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text_input=text, shift_input=shift):
    decrypt_text = ""
    for letter in text_input:
        position_in_alphabet = alphabet.index(letter)  # find the letter position in the alphabet
        decrypt_text += alphabet[position_in_alphabet - shift_input]  # shift the letter
    print(f"The coded text is : {decrypt_text}")


# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text_input=text, shift_input=shift)
elif direction == "decode":
    decrypt(text_input=text, shift_input=shift)


