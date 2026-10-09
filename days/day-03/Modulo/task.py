# print(10%3)
#
# user_number=int(input("Enter a no to check whether it's a even or odd: \n"))
#
# if user_number % 2 ==0:
#     print("The no. is even")
# else:
#     print("The no. is odd")

#print(15%8)

print("Welcome to the world where you want to check weather the number you care about is odd or even")
number = (input("Enter the number that you want to check weather it's even or odd: "))

if int(number) %2 ==0 :
    print(f"{number} is a even number")
elif int(number) %2 !=0 :
    print(f"{number} ia a odd number")
else:
    print("Invalid Input")
