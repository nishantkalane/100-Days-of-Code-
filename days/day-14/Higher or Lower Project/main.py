import random
import game_data
import art

def data_getter():
    data_for_item = random.choice(game_data.data)
    return data_for_item

def win_or_loss(user_choice,a_f,b_f):

    if (a_f > b_f and user_choice == 'a') or ( b_f > a_f and user_choice == 'b'):
        return True
    else:
        return False

score = 0
a_dic = data_getter()
b_dic = data_getter()
while a_dic == b_dic:
    b_dic = data_getter()

while(True):
    a_fol= a_dic['follower_count']

    b_fol= b_dic['follower_count']
    print(art.logo)

    if score > 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {a_dic['name']}, a {a_dic['description']}, from {a_dic['country']} ")

    print(art.vs)
    print(f"Compare B: {b_dic['name']}, a {b_dic['description']}, from {b_dic['country']} ")

    u_c = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

    result = win_or_loss(u_c,a_fol, b_fol)

    if result:
        score += 1
        a_dic=b_dic
        b_dic=data_getter()
        print("\n" * 10)
        continue
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score} ")
        break






































# import random
# import art
# import game_data
# #Print higher lower logo
#
# #get random assignment for a and b
# def random_assignment(num_aa,num_bb):
#     num_aa=random.randint(0,49)
#     num_bb=random.randint(0,49)
#     return num_aa,num_bb
# def compare_a(foll_a,foll_b):
#     if foll_a > foll_b:
#         return 1
#     elif foll_b>foll_a:
#         return 0
# def compare_b(foll_a,foll_b):
#     if foll_b > foll_a:
#         return 1
#     elif foll_a>foll_b:
#         return 0
#
#
# score=0
# num_a = random.randint(0,49)
# num_b = 0
#
# game_continue=False
# while not game_continue:
#     compare_aa = None
#     compare_bb = None
#     num_b=random.randint(0,49)
#     print("\n"*3)
#     #get data for A
#     A_print=game_data.data[num_a]
#     a_name=A_print["name"]
#     a_description=A_print["description"]
#     a_country=A_print["country"]
#     a_follower=A_print["follower_count"]
#     #get data for B
#     B_print=game_data.data[num_b]
#     b_name=B_print["name"]
#     b_description=B_print["description"]
#     b_country=B_print["country"]
#     b_follower=B_print["follower_count"]
#     print(art.logo)
#
#     #get compare A data
#     print(f"Compare A: {a_name}, a {a_description}, from {a_country} ")
#     #print vs logo
#     print(art.vs)
#     #get compare B data
#     print(f"Compare B: {b_name}, a {b_description}, from {b_country} ")
#
#     #ask user to predict
#     ask=input("Who has more followers? Type 'A' or 'B' ").lower()
#     #comapare and decide which is bigger
#     if ask=='a':
#      compare_aa=compare_a(a_follower,b_follower)
#
#     elif ask=='b':
#      compare_bb=compare_b(a_follower,b_follower)
#
#     if (compare_bb==1) or (compare_aa==1):
#         print("Congrats, you can move forward")
#         num_a = num_b
#         score+=1
#     elif (compare_aa==0) or (compare_bb==0):
#         print(f"Ahhn it is wrong, sorry , your score is {score}")
#         game_continue=True
#     #if it is correct assign the value of B to A and get new for B
#
#
#
#

