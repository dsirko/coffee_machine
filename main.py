from data import MENU, resources

# TODO: 1. Print report of a coffee machine resources

coffee_machine_is_on = True

current_resources = resources

money = 0
cur_water = current_resources['water']
cur_milk = current_resources['milk']
cur_coffee = current_resources['coffee']

while coffee_machine_is_on:

    # def check_if_enough_resources(drink):
    #     if drink in MENU:
    #         MENU[drink][""] -=


    def take_a_payment(user_drink, drink_cost):
        float(drink_cost)
        # current_resources.money = money

        print("Please insert coins.\n")
        current_quarters = int(input("how many quarters?:"))  # 25 cents
        current_dimes = int(input("how many dimes?:"))  # 10 cents
        current_nickels = int(input("how many nickels?:"))  # 5 cents
        current_pennies = int(input("how many pennies?:"))  # 1 cent

        total_payment = current_quarters * 0.25 + current_dimes * 0.10 + current_nickels * 0.05 + current_pennies * 0.01

        change = round(total_payment - drink_cost, 2)
        global money
        if change >= 0:
            money = money + drink_cost
            calculate_current_resouses()
            return f"Here is ${change} in change..\nHere is your {user_drink} ☕️. Enjoy!"
        else:
            return "Sorry that's not enough money. Money refunded."


    def calculate_current_resouses():
        global cur_water
        global cur_milk
        global cur_coffee
        cur_water -= MENU[user_choise_of_drink]['ingredients']['water']
        cur_milk -= MENU[user_choise_of_drink]['ingredients']['milk']
        cur_coffee -= MENU[user_choise_of_drink]['ingredients']['coffee']
        return cur_coffee, cur_water, cur_milk


    def prepare_resources_report():
        print (f"Water: {cur_water}ml\nMilk: {cur_milk}ml\nCoffee: {cur_coffee}g\nMoney: ${money}")

    user_choise_of_drink = input("What would you like? (espresso/latte/cappuccino):")

    if user_choise_of_drink == "off":
        print("Coffee machine shutdowned. Good bye!")
        coffee_machine_is_on = False

    if user_choise_of_drink == "report":
        prepare_resources_report()

    if user_choise_of_drink in MENU:
        # check_if_enough_resources("espresso")
        print(take_a_payment(user_choise_of_drink, MENU[user_choise_of_drink]['cost']))

