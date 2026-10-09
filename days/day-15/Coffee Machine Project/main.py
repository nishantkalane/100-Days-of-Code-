MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 150,
}


serve = True
money=0

def check_resources(coffee):

    """Checking if sufficient resources are available to make the drink"""
    check_count=0
    less= "none"
    if MENU[f'{coffee}']['ingredients']['water'] > resources['water'] :
        check_count =1
        less = "water"

    elif MENU[f'{coffee}']['ingredients']['coffee'] > resources['coffee'] :
        check_count =1
        less = "coffee"
    elif coffee != 'espresso' and MENU[f'{coffee}']['ingredients']['milk'] > resources['milk'] :
        check_count =1
        less = 'milk'
    if check_count == 1:
        return False,less
    else:
        return True,less

def coin_processing():
    """Asking to insert coins and calculating their total"""
    print("Please Insert Coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

def report_change(coffee):
    """After the transaction is successful resources are deducted using this function"""
    resources['water'] -= MENU[f'{coffee}']['ingredients']['water']
    if coffee !='espresso':
        resources['milk'] -= MENU[f'{coffee}']['ingredients']['milk']
    resources['coffee'] -= MENU[f'{coffee}']['ingredients']['coffee']

while serve:

    ask=input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    if ask == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")
        continue
    elif ask=="off":
        serve = False
        break

    elif ask in MENU:
        result_of_resources_available, ing = check_resources(ask)
        if result_of_resources_available == False:
            print(f"Sorry there is not enough { ing}")
            serve = False
            continue

    amount=coin_processing()
    cost =MENU[f'{ask}']['cost']

    if amount < cost:
        print("Sorry that's not enough money. Money refunded")

    elif amount >= cost:
        return_amount= amount-cost
        print(f"Here is ${ round(return_amount,2) } dollars in change")
        report_change(ask)
        money += cost
        print(f"Here is your {ask}. Enjoy!")

