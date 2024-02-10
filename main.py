
from data import MENU, resources

# TODO: 1. Print report of a coffee machine resources

coffee_machine_is_on = True

current_resources = resources
money = 0

while coffee_machine_is_on:

    # def check_if_enough_resources(drink):
    #     if drink in MENU:
    #         MENU[drink][""] -=

    def take_a_payment(drink_cost):
        float(drink_cost)
        # current_resources.money = money

        print("Please insert coins.\n")
        current_quarters = int(input("how many quarters?:"))  # 25 cents
        current_dimes = int(input("how many dimes?:"))  # 10 cents
        current_nickels = int(input("how many nickels?:"))  # 5 cents
        current_pennies = int(input("how many pennies?:"))  # 1 cent

        def calculate_payment(current_quarters, current_dimes, current_nickels, current_pennies):
            total_payment = current_quarters * 0.25 + current_dimes * 0.10 + current_nickels * 0.05 + current_pennies * 0.01
            return round(total_payment, 2)

        print(drink_cost)

        print(calculate_payment(current_quarters, current_dimes, current_nickels, current_pennies))

    def prepare_resources_report():
        print (f"Water: {current_resources['water']}ml\nMilk: {current_resources['milk']}ml\nCoffee: {current_resources['coffee']}g\nMoney: ${money}")

    user_choise_of_drink = input("What would you like? (espresso/latte/cappuccino):")

    if user_choise_of_drink == "off":
        print("Coffee machine shutdowned. Good bye!")
        coffee_machine_is_on = False

    if user_choise_of_drink == "report":
        prepare_resources_report()

    if user_choise_of_drink == "espresso":
        # check_if_enough_resources("espresso")
        take_a_payment(MENU[user_choise_of_drink]['cost'])
