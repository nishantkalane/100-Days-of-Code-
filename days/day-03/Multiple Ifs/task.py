print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=12
    elif age <= 18:
        bill= 18
    else:
        bill=12

    wants_photo=str(input("Do you want a photo? type y for yes and n for no \n"))
    if wants_photo == "y":
        bill +=3
    print(f"Your bill is $ {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
