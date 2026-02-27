tank = {
"water": 300,
"coffee": 100,
"milk": 200,
"profit": 0.00
}

espresso = {
"water": 100,
"coffee": 18,
"price": 1.50
}

latte = {
"water": 200,
"coffee": 24,
"milk": 150,
"price":2.50
}

cappuccino = {
"water": 250,
"coffee": 24,
"milk": 100,
"price": 3.00
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

menu = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino
}

def payment():
    print("Please insert coins.")
    quarters = (float(input("How many quarters? "))) * 0.25
    dimes = (float(input("How many dimes? "))) * 0.10
    nickels = (float(input("How many nickels? "))) * 0.05
    pennies = (float(input("How many pennies? "))) * 0.01
    
    coins_inserted = quarters + dimes + nickels + pennies
    return coins_inserted

while True:
        
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order.lower() == "report":
        print(f"Resources Left\nWater: {tank['water']}ml\nCoffee: {tank['coffee']}g\nMilk: {tank['milk']}ml\nProfit: ${tank['profit']}")

    elif order.lower() in menu:

        drink = menu[order.lower()]

        # Check resources
        for ingredient, amount_needed in drink.items():
            if ingredient == "price":
                continue
            if tank[ingredient] < amount_needed:
                print(f"Sorry there isn't enough {ingredient}")
                break
        else:
            coins_inserted = round(payment(), 2)
            price = drink["price"]

            if coins_inserted >= price:
                print(f"Here is your {order} ☕. Enjoy!")
                if coins_inserted > price:
                    print(f"Here is ${round(coins_inserted - price, 2)} in change")
                    tank["profit"] += price

                for ingredient in drink:
                    if ingredient != "price":
                        tank[ingredient] -= drink[ingredient]

            else:
                print("Sorry that's not enough money. Money refunded.")

    elif order == "off":
        print("Machine turning off.")
        break 

