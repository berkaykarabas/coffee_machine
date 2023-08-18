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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def control_level(coffe_type_remain):
    for item in coffe_type_remain:
        if coffe_type_remain[item]< resources[item]:
            print(f"It isn't enough {item} level please call +955050005500")
            return False
    return True
def money_receipt():
    total = int(input("how many you will put to the machine querters?")) * 0.25
    total += int(input("how many you will put to the machine dimes?")) * 0.1
    total += int(input("how many you will put to the machine querters?")) * 0.05
    total += int(input("how many you will put to the machine querters?")) * 0.01
    return total
def money_suciffient(money, cost):
    if money >= cost:
        exchange = round(money - cost, 2)
        print(f"Here is your exchange {exchange}")
        return True
    else:
        print("there is not enough money please refill")
        return False
def make_coffe(name, coffe_type_remain):
    for item in coffe_type_remain:
        resources[item]-=coffe_type_remain[item]
    print(f"Here is your coffee {name}")
is_on: True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f"water is: {resources['water']} ml.")
        print(f"milk is: {resources['milk']} ml.")
        print(f"coffee is: {resources['coffee']} g.")
        print(f"money is: {profit} $.")
    else:
        drink = MENU[choice]
        if control_level(drink["ingredients"]):
            money = money_receipt()
            cost = drink["cost"]
            if money_suciffient(money, cost):
                make_coffe(choice,drink["ingredients"])
