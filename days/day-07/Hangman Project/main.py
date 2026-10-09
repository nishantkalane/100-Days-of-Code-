import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
print(hangman_art.logo)
chosen_word = random.choice(word_list)
print(chosen_word)


lives=6
placeholder = ''
for ch in chosen_word:
    placeholder+= "_"
print(placeholder)

lenth_of_word=len(placeholder)
flag = False
i=0
matched=''
while flag == False:
    guess = input("Guess a letter: ").lower().strip()
    display = ''
    if guess in matched:
        print(f"You have already guessed the letter {guess}")
        print(hangman_art.stages[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        if guess in chosen_word:
                for ch in chosen_word:
                    if ch == guess:
                        display += ch
                        matched +=ch
                    elif ch !=guess and ch in matched:
                            display +=ch
                    else:
                        display += "_"

                print(f"Word to guess {display}")
                print(hangman_art.stages[lives])
                print(f"****************************{lives}/6 LIVES LEFT****************************")
                if '_'not in display:
                    flag=True
                    print("You WON")
        else:
            lives -=1
            print(f"You have guessed {guess}, that's not in the word. You lose a life")
            print(hangman_art.stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")
            if lives==0:
                print(f"IT WAS {chosen_word}")
                print("You lose")
                flag=True






















#
#
#
# import random
#
# # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# import hangman_words
# lives = 6
#
# # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# import hangman_art
# print(hangman_art.logo)
# chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)
#
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)
#
# game_over = False
# correct_letters = []
#
# while not game_over:
#
#     # TODO-6: - Update the code below to tell the user how many lives they have left.
#     print(f"****************************{lives}/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()
#
#     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in correct_letters:
#         print(f"You have already entered {guess} letter try again!")
#     display = ""
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print("Word to guess: " + display)
#
#     # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#     #  e.g. You guessed d, that's not in the word. You lose a life.
#
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"{guess} is not in the chosen word, You lose a life.")
#         if lives == 0:
#             game_over = True
#
#             # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
#             print(f"***********************YOU LOSE**********************")
#             print(f"The correct word you were trying to guess is {chosen_word}")
#
#     if "_" not in display:
#         game_over = True
#         print("****************************YOU WIN****************************")
#
#     # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
#     print(hangman_art.stages[lives])
