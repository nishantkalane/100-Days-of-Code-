colours = ["red", "blue"] #list

#dictionary
dictionary ={
    "diary":"brown",
    "gita":"red",
    "dsa":"yellow",
    "White_board":"geen",
    1:2
}

#retrieve items from a dictionary
print(dictionary["gita"])

#empty dictionary
dict = {
}

#edit a value of a key in dictionary
dictionary["White_board"]="green"
print(dictionary["White_board"])
print()

print("loop through dictionary to get keys")
for key in dictionary:
    print(key)
print()
print("loop through dictionary to get values")
for key in dictionary:
    print(dictionary[key])



# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
#
# colours={
#     "apple":"red",
#     "pear":"green",
#     "banana":"yellow"
# }
# #printint a value of a key
# print(colours["pear"])
# #empty list
# my_empty_dictionary = {}
# #adding new items to a list
# colours["peach"]="pink"
# print(colours)
# for key in colours:
#     print(colours[key])