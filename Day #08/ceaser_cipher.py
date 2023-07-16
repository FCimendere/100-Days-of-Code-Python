"""
PRACTISE: Function parameters, lists
Project : Ceaser Cipher 
A Caesar cipher is a simple method of encoding/decoding messages. 
Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding/decoding alphabet. 
A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.
"""

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encoded_text = []
    new_text = []

    #collecting the index info of the text
    #before alphabet manipulatio
    for letter in text:
        index_no = alphabet.index(letter)
        new_text.append(index_no)

    #alphabet manipulated based on shift number.
    for i in range(shift):
        popped_letter = alphabet.pop(0)
        alphabet.append(popped_letter)

    #changing every letter of text with new alphabet letters
    for i in range(len(text)):
        new_index = new_text[i]
        new_letter = alphabet[new_index]
        encoded_text.append(new_letter)
        my_string = ''.join(map(str, encoded_text))
    print(f"The encoded text is {my_string}")


def decrypt(text, shift):

    decrypted_message = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += letter
    print(f"The decoded text is {decrypted_message }")


#control of decode or encode
def direction_control(direction):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)


#call the encrytion  or decrytion function
direction_control(direction)
