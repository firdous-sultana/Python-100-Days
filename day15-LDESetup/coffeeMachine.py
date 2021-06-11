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

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredient):
    '''Returns true when order can be made, False if ingredients are sufficient'''
    for item in order_ingredient:
        if(order_ingredient[item] >= resources[item]):
            print("Sorry there is not enough {}.".format(item))
            return False
        # else:
            # resources[item] -= order_ingredient[item]
    # return resources[item]
    return True

def is_transaction_successful(cost_input, drink_cost):
    '''Return True if payment is accepted, or False if money is insufficient'''
    if(cost_input >= drink_cost):
        change = round(cost_input - drink_cost, 2)
        print("Here is ${} dollars in change.".format(change))
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def process_coins():
    '''Total calculated from coins inserted'''
    print("Please insert coins.")
    quar = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pen = float(input("how many pennies?: "))

    coin_inserted = (0.25 * quar) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pen)
    return coin_inserted


def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients frim the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your {}. Enjoy!".format(drink_name))

on_ = True


while on_:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if(choice == 'off'):
        on_ = False
    elif(choice == 'report'):
        print("Water: {}ml".format(resources['water']))
        print("Milk: {}ml".format(resources['milk']))
        print("Coffee: {}g".format(resources['coffee']))
        print("Money: ${}".format(money))
    else:
        drink = MENU[choice]
        if(is_resource_sufficient(drink['ingredients'])):
            payment = process_coins()
            if(is_transaction_successful(payment, drink['cost'])):
                make_coffee(choice, drink['ingredients'])
    
    