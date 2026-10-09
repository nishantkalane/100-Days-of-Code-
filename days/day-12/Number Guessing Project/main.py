import art
import random

def guess_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    guess_number=random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower().strip()
    no_of_attempts=0
    if difficulty =='easy':
        no_of_attempts =10
    elif difficulty =='hard':
        no_of_attempts =5
    else:
        print("Give valid input")
    while no_of_attempts > 0:
        print(f"You have {no_of_attempts} remaining to guess the number.")
        user_guess=int(input("Make a guess: "))
        if user_guess == guess_number:
            print(f"You got it, The answer is {user_guess}")
            break
        else:
            if user_guess > guess_number:
                print("Too High.\nGuess Again.")
            if user_guess < guess_number:
                print("Too Low.\nGuess Again.")
            if no_of_attempts==0:
                print("You ran out of guesses. Better luck next time.")
            no_of_attempts -=1

guess_game()
game_is_over = False
while not game_is_over:
    print("\n"*3)
    ask=input("Type 'y' if you want to play again else type 'n': ").lower().strip()
    if ask =='y':
        print("\n"*100)
        guess_game()
    else:
        game_is_over=True




























# def guessing_game():
#     print(art.logo)
#     print("Welcome to the Number Guessing Game!")
#     random_no=random.randint(1,100)
#
#     hard_easy=input("Choose a difficulty. Type 'easy' or 'hard' :").lower()
#
#     no_of_guesses=0
#     if hard_easy=='easy':
#         no_of_guesses=10
#     elif hard_easy=='hard':
#         no_of_guesses=5
#     else:
#         print("Enter correct value")
#     game_continue=False
#     while not game_continue:
#         if no_of_guesses !=0:
#             while no_of_guesses!=0:
#                 print(f"You have {no_of_guesses} number of guesses left")
#                 guess=int(input("Make a guess: "))
#                 if random_no == guess:
#                     no_of_guesses = 1
#
#                     print(f"You got it the answer was {random_no} ")
#                     game_continue=True
#                 elif random_no > guess:
#                     print("Too low.")
#                     print("Guess Again")
#                 elif random_no < guess:
#                     print("Too High")
#                     print("Guess Again")
#
#                 no_of_guesses -=1
#         else:
#             game_continue=True
#             print("You ran out of guesses, you lose.")
# continue_game=False
# while not continue_game:
#     print("\n"*3)
#     play_game=input("Do you want to play a guessing game ? type 'y' for yes and 'n' for no: ").lower()
#     if play_game=='y':
#         guessing_game()
#     elif play_game=='n':
#         continue_game=True
#         print("Thankyou for visiting")
#     else:
#         print("Give valid input")
#


