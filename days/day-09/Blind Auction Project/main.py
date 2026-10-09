# TODO-1: Ask the user for input
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
# TODO-2: Save data into dictionary {name: price}

import art
blind_auction_dict={
    #"person_name":"bid"
}

def compare():
    for key in blind_auction_dict:
        max=0
        max_key=key
        if blind_auction_dict[key]>max:
            max =blind_auction_dict[key]
            max_key=key
    print(f"Winner is {key} with bid of ${blind_auction_dict[key]}")

print(art.logo)

flag= True

while flag==True:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    blind_auction_dict[name] = bid
    other_bidders = input("Are there other bidders? Type \"yes\" or \"no\" : ").strip().lower()
    if other_bidders=='yes':
        print("\n"*100)
    elif other_bidders =="no":
        flag=False
    else:
        print("Invalid Input!")
        flag=False

compare()















# import art
# print(art.logo)
# auction_d={}
# def charles():
#     global game_done
#     bidders=input("Are there more bidder? type 'yes' or 'no'. \n ").lower()
#     if bidders=="yes":
#         print("\n"*50)
#     if bidders=="no":
#         game_done=False
#         maxn=0
#         winner=""
#         for nav,score in auction_d.items():
#             if score > maxn:
#                 maxn=score
#                 winner=nav
#
#         print(f"The winner is {nav}  with a bid of ${maxn}")
# game_done =True
# while game_done==True:
#     name=input("What is your name?: ").lower()
#     bid=int(input("What is your bid?: $"))
#
#     auction_d[name]=bid
#     charles()

