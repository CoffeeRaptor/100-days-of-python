import string
from encodings.utf_7 import encode
from operator import index

alphabet = list(string.ascii_lowercase)


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount = shift_amount * -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type encode to encrypt, type decode to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode = direction)
    restart = input("Again?\n").lower()
    if restart == "no":
        should_continue = False
        print("Ciao")