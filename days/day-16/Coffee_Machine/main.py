from importlib.resources import is_resource

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    ask = input(f"What would you like {options}: ")
    if ask == "off":
        is_on = False
    elif ask == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_maker.is_resource_sufficient(menu.find_drink(ask)) and money_machine.make_payment(menu.find_drink(ask).cost):
        coffee_maker.make_coffee(menu.find_drink(ask))

# is_on= True
#
# while  is_on:
#     options = menu.get_items()
#     choice= input(f"What would you like ? ({options}): ")
#     if choice == "off":
#         is_on = False
#     if choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)


