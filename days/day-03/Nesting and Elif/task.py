print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age? \n"))
    if age <=18:
        print("Pay $10")
    else:
        print("Pay $15")
else:
    print("Sorry you have to grow taller before you can ride.")



print("Welcome to the world of greatness !")
read_books = (input("Do you read books ? type yes or no")).strip().lower()
if read_books =='yes':
    lessons=input("Do you follow them yes or no ? ").strip().lower()
    if lessons == "yes":
        print("Great man you are good going, increase the practice and you will win the world")
    else:
        print("Start practicing dude it is worth it")
else:
    print("Good then do whatever you want")