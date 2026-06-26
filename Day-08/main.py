#Caesar Cipher Program
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Create a Function
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    #Convert the shift number to negative as decoding needs to be backward
    if encode_or_decode == "decode":
        shift_amount *= -1

    #Shift each alphabet according to the shift number
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        #Print the letters that are not in alphabet list as it is
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

#Ask for the input and stop when user says no to continue
to_continue = "yes"
while to_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    to_continue = input("Do you want to continue: 'yes' or 'no':\n").lower()



