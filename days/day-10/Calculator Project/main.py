
# TODO: 1) Write functions for caluclations
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

# TODO: 2) Add calculations in a dictionary

calculation_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

# TODO:3) Using the dictionary operators to perform calculations:
import art
print(art.logo)
def output(first_num):
    print("+\n-\n*\n/")
    mathematical_operator = input("Pick and operation: ")
    second_number = int(input("What's the second number: "))
    result = calculation_dict[mathematical_operator](first_num, second_number)
    return (result, (f"{first_num} {mathematical_operator} {second_number} = {result}"))

first_number=int(input("What's the first number:  "))
i,final_result=output(first_number)
print(final_result)


flag=True
while flag==True:
    ask = input(f"Type 'y' to continue calculating with {i}, or type 'n' to start a new calculation.").strip().lower()
    if ask =="y":
        first_num=i
        i,final_result=output(first_num)
        print(final_result)

    elif ask=="n":
        first_number=int(input("What's the first number: "))
        i,f_result=output(first_number)
        print(f_result)






























#
# cal_dict={
#     "+":add,
#     "-":sub,
#     "/":div,
#     "*":mul,
# }
#






















































































































# def add(n1, n2):
#     """Subtract"""
#     return n1 + n2
# def sub(n1,n2):
#     """Add"""
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2
#
# cal_dict={
#     "+":add,
#     "-":sub,
#     "/":div,
#     "*":mul,
# }
# import art
# def caluclator():
#     print(art.logo)
#     calculation_over = True
#     first_number = float(input("Type the first number? : "))
#     while calculation_over == True:
#         for symbol in cal_dict:
#             print(symbol)
#         mathematical_op = input("Pick an operation : ")
#         second_number = float(input("Type the next number? : "))
#         answer_1 = float(cal_dict[mathematical_op](first_number, second_number))
#         print(answer_1)
#         want_continue = input( "Type yes if want to continue working with the previous result or type no if don't want to : ").lower()
#         if want_continue == "yes":
#             first_number=answer_1
#         if want_continue == "no":
#             # calculation_over=False
#
#             calculation_over == False
#             print("" * 20)
#             caluclator()
# caluclator()