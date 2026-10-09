
#tip calculator project

print("Welcome to the tip calculator ")

bill= input("what was your bill ? ")
people=input("Between how many people the bill shall be distributed? ")
percent=input("How much percent would you like to pay the tip ?")
extra= int(bill) * int(percent)/100

total_bill=extra+int(bill)
by_per_person=round(total_bill/int(people),2)

print(f"Each person should pay : {by_per_person}")

































# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
#
#
# bill_with_tip = bill+ ( bill*(tip/100) )
# bill_per_person= bill_with_tip/people
# print(f"your total bill per person is {round(bill_per_person,2)}")