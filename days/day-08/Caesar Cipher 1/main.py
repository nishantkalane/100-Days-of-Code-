alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message= input("Type your message: ")
shift =int(input("Type the shift number: "))
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    encrypted_text= ""
    encrypted_text_index=[]
    rounded_value=0
    for ch in original_text:
        k= alphabet.index(ch)
        encrypted_text_index.append(k)
    for i in encrypted_text_index:
        i += shift_amount
        i %=26
        encrypted_text +=alphabet[i]
    print(f"Here's the encoded result: {encrypted_text}")


# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(message,shift)




















# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# def encrypt(original_text, shift_amount):
#     index=[]
#     encrypted_text=""
#     for letter in original_text:
#         no=alphabet.index(letter)
#         no += shift_amount
#         no %=len(alphabet)
#         index.append(no)
#     for number in index:
#         encrypted_text +=alphabet[number]
#     print(encrypted_text)
# encrypt(original_text=text,shift_amount=shift)