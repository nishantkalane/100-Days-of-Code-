# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >=130:
#     print("You can ride")
# else:
#     print("Sorry you cannot ride this one")

print("Welcome to the library !!")
cost = 1200
hall= input("In which hall are you? 'a' or 'b' ").strip().lower()

if hall =='a':
    print(f"you have normal enviornment at {cost}")
elif hall=='b':
    print(f"you hav awesome enviornment at {cost} and great chairs")
else:
    print("You aren't in library for sure")