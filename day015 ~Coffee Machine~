from info import MENU, resources


def order():
    while True:
        choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

        for item in MENU:
            if item == choice:
                return choice
        else:
            if choice == "report":
                for ingredient in resources['ingredients']:
                    print(f"{ingredient:<6}:", end="")
                    print(f"{resources['ingredients'][ingredient]}")
                print(f"money :{resources['money']}")
            elif choice == "off":
                return choice
            else:
                print("Sorry, that's not a valid command.")


def payment(drink):
    price = MENU[drink]['cost']
    print(f"The {drink.capitalize()} is $", end="")
    print("%.2f." % price)

    print("Please insert coins:")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes    = 0.10 * int(input("         dimes?   : "))
    nickles  = 0.05 * int(input("         nickles? : "))
    pennies  = 0.01 * int(input("         pennies? : "))

    total = quarters + dimes + nickles + pennies

    if total >= price:
        change = total - price
        resources['money'] += price
        if change != 0:
            print(f"Here's your change: $", end="")
            print('%.2f' % change)
        else:
            print("You gave the exact amount. There's no change.")
        return True
    else:
        print("Looks like that's not enough money.")
        return False


def resources_usage(drink):
    for ingredient in resources['ingredients']:
        resources['ingredients'][ingredient] -= MENU[drink]['ingredients'][ingredient]
        if resources['ingredients'][ingredient] < 0:
            print(f"Sorry, there is not enough {ingredient} to make your {drink}")
            resources['ingredients'][ingredient] += MENU[drink]['ingredients'][ingredient]
            return False

    return True


# main
print("Welcome to the Coffee Machine!")
while True:
    drink_choice = order()

    if drink_choice == "off":
        break
    else:
        has_enough_resources = resources_usage(drink_choice)
        payment_is_valid = payment(drink_choice)

        if has_enough_resources and payment_is_valid:
            print(f"Here is your {drink_choice} ☕. Enjoy!")

print("Thank you for using the Coffee Machine.")
print("Have a great day!")
