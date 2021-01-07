from menu import MENU
approved_commands = [
    "espresso",
    "latte",
    "cappucio",
    "off",
    "report"
]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def main():
    while True:
        user_choice = get_user_input()
        print("\nYour choice is %s" % (user_choice))

        if user_choice == "off":
            print("Shutting off")
            break
        elif user_choice == "report":
            print_report()
        else:
            sufficientcy = check_sufficientcy(user_choice)
            if sufficientcy:
                totale_user_values = process_coins()
                check_price(user_choice, totale_user_values)


def get_user_input():
    user_choice = input("\nWhat would you like? \n").lower()
    while user_choice not in approved_commands:
        user_choice = input(
            "\nInvalid parameter.\nWhat would you like? \n").lower()
    return user_choice


def print_report():
    print(
        """
        Water: %sml
        Milk: %sml
        Coffee: %sg
        Money: $%s
        """ % (resources["water"], resources["milk"], resources["coffee"], resources["money"])
    )


def check_sufficientcy(coffee_type):
    for ingredient in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][ingredient] <= resources[ingredient]:
            return True
        else:
            print("Sorry, we are out of resources")
            return False


def pure_coffee(coffee_type):
    pass


def process_coins():
    quaters = float(input("Enter quaters: "))
    dimes = float(input("Enter dimes: "))
    nickels = float(input("Enter nickles: "))
    pennies = float(input("Enter pennies: "))
    return quaters*0.25+dimes*0.1+nickels*0.05+pennies*0.01


def check_price(coffee_type, value):
    if MENU[coffee_type]["cost"] <= value:
        resources["money"] = MENU[coffee_type]["cost"]
        print("Change is %s" % (value-MENU[coffee_type]["cost"]))
        for ingredient in MENU[coffee_type]["ingredients"]:
            resources[ingredient] = resources[ingredient] - \
                MENU[coffee_type]["ingredients"][ingredient]
        print("Enjoy your coffee!")

        return True
    else:
        print("Insufficient amount of money")
        print("Money refunded")
        return False


main()
