import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l_pass = int(input("How many letters would you like in your password? "))
l_sym = int(input("How many symbols would you like?"))
l_num = int(input("How many numbers would you like ? "))

password= []

for i in range(l_pass) :
    password.append(random.choice(letters))
for j in range(l_sym):
    password.append(random.choice(symbols))
for k in range(l_num):
    password.append(random.choice(numbers))
random.shuffle(password)
result ="".join(map(str,password))
print(result)
































 #
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# password_list=[]
#
# for unit in range(0,nr_letters ):
#     choice=random.choice(letters)
#     password_list.append(choice)
#
# for unit in range(0,nr_symbols ):
#     sy=random.choice(symbols)
#     password_list.append(sy)
#
# for unit in range(0,nr_numbers ):
#     nu=random.choice(numbers)
#     password_list.append(nu)
#
# random.shuffle(password_list)
# password="".join(password_list)
# print(password)
