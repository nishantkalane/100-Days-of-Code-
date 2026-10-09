print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure island \nYour mission is to find the treasure ")
one= input('You\'re at a cross road. Where do you want to go'
      '\nType "left" or "right"\n'.center(80)).lower().strip()

if one =="left":
    two=input('You\'ve come to a lake. THere is an island in the middle of the lake.'
              '\nType "wait" to wait for a boat. Type "swim to swim across.\n'.center(80)).strip().lower()
    if two =="wait":
        three=input('You arrive at the island unharmed. There is a house with 3 doors'
                    '\none red, one yellow and one blue. which colour do you choose?\n '.center(80)).strip().lower()
        if three =="red":
            print("you found the treasure! You Win!")
        elif three =="blue":
            print("You went to village of papa smurf try again!")
        elif three=="yellow":
            print("You fell off the edge, try again!")
        else:
            print("give valid input")
    else:
        print("Alligator attacked you, you died !!")
else:
    print("You fell in hole try again")





























# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# which_way=input("Type L if you want to go left towards lava with a suite or type R if you want to cross a river that has no water with boat \n").lower()
# if which_way=="r":
#     print("You Move Ahead" )
#     which_food=input("Being and Indian will you prefer Spicy food or not Spicy food: type S for spicy food and N for not spicy food \n").lower()
#     if which_food =="s":
#         print("You Move Ahead")
#         which_room=input("Which room would you like to enter:type F for room of fire, type W for room of water, type L for room with 1 week empty stomach Lion \n").lower()
#         if which_room=="l":
#             print("You win")
#         else:
#             print("Game Over")
#     else:
#         print("Game over")
# else:
#     print("Game over")
