from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input(
    'Type "encode" to encrypt. Type "decode" to decrypt: \n'
).strip().lower()
message= input("Type your message: \n").strip().lower()
shift =int(input("Type the shift number: \n"))
def encrypt(original_text, shift_amount):
    encrypted_text= ""
    encrypted_text_index=[]

    for ch in original_text:
        #getting index of letter from original letter
        index_amount= alphabet.index(ch)
        # adding the shift amount
        index_amount +=shift_amount
        # rounding to adjust the out of bound case
        index_amount %= 26
        encrypted_text +=alphabet[index_amount]

    print(f"Here's the encoded result: {encrypted_text}")

def decrypt(original_text,shift_amount):
    decrypted_text=""
    decrypted_text_index=[]
    for ch in original_text:
        #getting the index amount
        index_amount= alphabet.index(ch)
        #Subtracting the index amount
        index_amount =index_amount -shift_amount
        #rounding the offsets
        index_amount %=26
        decrypted_text +=alphabet[index_amount]
    print(f"Here's the decoded result: {decrypted_text}")


def caesar(inputd):
    if inputd== "encode":
        encrypt(message, shift)
    if inputd == "decode":
        decrypt(message, shift)
caesar(direction)

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
# #  by the shift amount and print the decrypted text.


# # TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
# #  Use the value of the user chosen 'direction' variable to determine which functionality to use.

#
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
#
# def caesar(orginal_text,shift_amount, encode_or_decode):
#     if encode_or_decode == "decode":
#         shift_amount *= -1
#     cipher_text = ""
#     for letter in orginal_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {cipher_text} ")
#
# caesar(orginal_text=text, shift_amount=shift,encode_or_decode=direction)
#


#     decipher_text=""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {decipher_text}")