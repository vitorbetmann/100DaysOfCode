from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    order = menu.find_drink(choice)

    if order == "off":
        machine_is_on = False
        
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    elif order is not None:
        order = menu.find_drink(choice)
        can_make_coffee = coffee_maker.is_resource_sufficient(order)
        can_pay = money_machine.make_payment(order.cost)
        if can_make_coffee and can_pay:
            print(f"Enjoy your {order.name}!")
            
    else:
        continue

print("Thank you for using the Coffee Machine!")
