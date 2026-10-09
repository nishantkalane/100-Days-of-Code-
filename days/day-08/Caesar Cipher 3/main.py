
# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
# TODO-2: What happens if the user enters a number/symbol/space?
from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input(
    'Type "encode" to encrypt. Type "decode" to decrypt: \n'
).strip().lower()

message= input("Type your message: \n").strip().lower()
shift =int(input("Type the shift number: \n"))
def encrypt(original_text, shift_amount):
    encrypted_text= ""


    for ch in original_text:
        if ch in alphabet:
            #getting index of letter from original letter
            index_amount= alphabet.index(ch)
            # adding the shift amount
            index_amount +=shift_amount
            # rounding to adjust the out of bound case
            index_amount %= 26
            encrypted_text +=alphabet[index_amount]
        else:
            encrypted_text +=ch

    print(f"Here's the encoded result: {encrypted_text}")

def decrypt(original_text,shift_amount):
    decrypted_text=""

    for ch in original_text:
        if ch in alphabet:
            #getting the index amount
            index_amount= alphabet.index(ch)
            #Subtracting the index amount
            index_amount =index_amount -shift_amount
            #rounding the offsets
            index_amount %=26
            decrypted_text +=alphabet[index_amount]
        else:
            decrypted_text +=ch
    print(f"Here's the decoded result: {decrypted_text}")


def caesar(inputd):
    if inputd== "encode":
        encrypt(message, shift)
    if inputd == "decode":
        decrypt(message, shift)
if direction == "encode" or direction=="decode":
    caesar(direction)
else:
    print("Give correct input")
    direction = input(
        'Type "encode" to encrypt. Type "decode" to decrypt: \n'
    ).strip().lower()

    message = input("Type your message: \n").strip().lower()
    shift = int(input("Type the shift number: \n"))
    caesar(direction)
# TODO-3: Can you figure out a way to restart the cipher program?
flag= False
while flag==False:
    ask=input('Type yes if you want to go again. else type "no" \n').lower().strip()


    if ask =="yes":
        direction = input(
            'Type "encode" to encrypt. Type "decode" to decrypt: \n'
        ).strip().lower()

        message = input("Type your message: \n").strip().lower()
        shift = int(input("Type the shift number: \n"))
        if direction == "encode" or direction == "decode":
            caesar(direction)
        else:
            print("Give correct input")
            direction = input(
                'Type "encode" to encrypt. Type "decode" to decrypt: \n'
            ).strip().lower()

            message = input("Type your message: \n").strip().lower()
            shift = int(input("Type the shift number: \n"))
            caesar(direction)
    elif ask=="no":
        flag=True
    else:
        print("Wrong input")
#
#
#
# # TODO-1: Import and print the logo from art.py when the program starts.
# import art
# print(art.logo)
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# # TODO-2: What happens if the user enters a number/symbol/space?
#
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#
#     for letter in original_text:
#         if letter in alphabet:
#             if encode_or_decode == "decode":
#                 shift_amount *= -1
#
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#         else:
#             output_text +=letter
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
# # TODO-3: Can you figure out a way to restart the cipher program?
#
#
#
# game_over=True
# while  game_over==True :
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#
#     redo = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
#
#     if redo=="no":
#         game_over=False
#         print("Thank you.")