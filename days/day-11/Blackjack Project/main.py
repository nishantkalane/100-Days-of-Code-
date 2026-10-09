import random
import art





def game():
    def deal_card():
        """Returns a random card from a deck of cards"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        ran = random.choice(cards)
        return ran

    def calculate_score(cards):
        """"Takes the list of cards and return their sum"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(c_score, u_score):
        print(f"Your cards were {user_card}, and your score {u_score}")
        print(f"Computer cards were {computer_card}, and computer score is {c_score}")
        if c_score == u_score:
            print("It's a draw")
        elif c_score == 0:
            print("You Lost")
        elif u_score == 0 and c_score != 0:
            print("You won")
        elif u_score > 21:
            print("You Lost")
        elif c_score > 21:
            print("You Won")
        elif u_score > c_score:
            print("You won")
        else:
            print("You Lost")
    user_card =[]
    computer_card=[]
    comp_score =-1
    user_score = -1
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())



    game_over = False
    while not game_over :
        comp_score = calculate_score(computer_card)
        user_score = calculate_score(user_card)

        print(f"Your cards are {user_card}, and score is {user_score}")
        print(f"Computer's First card is {computer_card[0]}")

        if comp_score == 0 or (user_score >21) or user_score ==0:
            game_over =True
        else:
            draw_another_card=input("Do you want to draw another card 'y' or 'n' ? " ).lower().strip()
            if draw_another_card =='y':
                user_card.append(deal_card())
            else:

                game_over =True


    while comp_score !=0 and comp_score <17:
        computer_card.append(deal_card())
        comp_score = calculate_score(computer_card)

    compare(comp_score,user_score)
print(art.logo)
game()

play_game= True

while  play_game :
    print("\n"*2)
    ask = input("Do you want to play again type 'y' for yes and 'n' for no: " )
    if ask == "y":
        print("\n"*100)
        print(art.logo)
        game()
    else:
        play_game= False
        print("Do visit again")























# def black_jack_game():
#     def deal_card():
#         """This functions deals a random card"""
#         cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#         card = random.choice(cards)
#         return card
#     def compare(us,cs):
#         if us==cs:
#             return "It's a draw"
#         elif cs==0:
#             return "You lost computer has a blackjack"
#         elif us==0:
#             return "You Win, you have a blackjack"
#         elif us >21:
#             return "You lost"
#         elif cs >21 :
#             return "You win, computer goes over"
#         else:
#             if us>cs:
#                 return "You win"
#             elif cs>us:
#                 return "You lost"
#     def calculate_score(cards):
#         """This functions takes a list of cards and return the total score of the cards, it is also used to deal with blackjack situation and to replace 11 with 1 if it goes above 21"""
#         if 11 in cards and 10 in cards and len(cards)==2:
#             return 0
#         if 11 in cards and sum(cards)>21:
#             cards.remove(11)
#             cards.append(1)
#         return sum(cards)
#     print(art.logo)
#     user_cards=[]
#     computer_cards=[]
#     computer_current_score=-1
#     user_current_score=-1
#     is_game_over = False
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#     while not is_game_over:
#
#
#
#         user_current_score=calculate_score(user_cards)
#         computer_current_score=calculate_score(computer_cards)
#         print(f"your cards{user_cards}, and your total is {user_current_score}")
#         print(f"computer's first card is {computer_cards[0]}")
#         if ((user_current_score==0) or (computer_current_score==0) ) or (user_current_score > 21):
#             is_game_over =True
#         else:
#             play_game=input("Do you want to continue playing the game, type y for yes and n for no : ").lower()
#
#             if play_game=="y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over=True
#     while computer_current_score != 0 and computer_current_score <17 :
#         computer_cards.append(deal_card())
#         computer_current_score=calculate_score(computer_cards)
#     print(f"Your final hand is : {user_cards}, your final scor is {user_current_score}")
#     print(f"Computer's final hand is: {computer_cards}, computer's score is {computer_current_score}")
#     print(compare(us=user_current_score,cs=computer_current_score))
#
#
# p_g=False
# while not p_g:
#     print("\n"*1)
#     play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
#     if play_game=='y':
#         black_jack_game()
#     elif play_game=='n':
#         p_g=True
#     else:
#         print("Give correct input")
#
#
