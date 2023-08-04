from coffee_menus import MENU
from coin_list import MONEY
from coffee_logos import m, e, l, c

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

is_on = True
profit = 0

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def payment_calculation():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * MONEY.get("quarter")
    total += int(input("How many dimes?: ")) * MONEY.get("dime")
    total += int(input("How many pennies?: ")) * MONEY.get("penny")
    total += int(input("How many nickels?: ")) * MONEY.get("nickel")
    return total


def is_money_sufficient(inserted_money, drink_cost):
    if inserted_money < drink_cost:
        inserted_money = round(inserted_money,2)
        print(f"Sorry there is not enough money. ${inserted_money} will be refunded.\n")
        return False
    else:
        change = round((inserted_money - drink_cost), 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} enjoy!\n")
    if drink_name == "espresso":
        print(e)
    elif drink_name == "latte":
        print(l)
    elif drink_name == "cappuccino":
        print(c)


print(m)
while is_on:
    choice = input("What would you like to drink?(espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"milk: {resources['milk']}ml")
        print(f"money: ${profit}")
    else:
        drink = MENU.get(choice)
        if resource_sufficient(drink["ingredients"]):
            payment = payment_calculation()
            if is_money_sufficient(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])




