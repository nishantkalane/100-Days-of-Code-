
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps=[rock, paper, scissors]
my_c= (input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if my_c in ['0','1','2'] :
    my_cc = int(my_c)
    print(rps[my_cc])

    com_no= random.randint(0,2)
    print(f"Computer chose: \n {rps[com_no]}")

    if (my_cc== 0 and com_no == 0) or (my_cc== 1 and com_no == 1) or (my_cc== 2 and com_no == 2):
        print("Draw")
    elif (my_cc== 0 and com_no == 2) or (my_cc== 1 and com_no == 0) or (my_cc== 2 and com_no == 1):
        print("You Win")
    elif(my_cc== 0 and com_no == 1) or (my_cc== 1 and com_no == 2) or (my_cc== 2 and com_no == 0):
        print("You lost")

else:
    print("undefined")




























# rps_list=[rock,paper,scissors]
#
#
# your_choice= int(input("What is your choice:type 0 for rock, type 1 for paper and 2 for sissors: \n"))
#
# if your_choice >0  and your_choice <2:
#     print(f"Your Choice:{rps_list[your_choice]}")
#
#
# random_int=random.randint(0,2)
# computer_choice= rps_list[random_int]
# print(f"Device choice {computer_choice}")
#
# if your_choice <0  or your_choice >2:
#     print("Give valid input")
# elif (random_int==0 and your_choice==0 ) or (random_int==2 and your_choice==2 ) or (random_int==1 and your_choice==1 ):
#     print("draw")
# elif (random_int==0 and your_choice==2 ) or (random_int==2 and your_choice==1 ) or (random_int==1 and your_choice==0 ):
#     print("You Lost")
# elif (random_int==2 and your_choice==0 ) or (random_int==1 and your_choice==2 ) or (random_int==0 and your_choice==1 ):
#     print("You Win")
# else:
#     print("Give correct input ")
