class Coffee:
    def __init__(self, water, coffee, milk = 0, price = 0.00, profit = 0.00):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.price = price
        self.profit = profit 

tank = Coffee(water = 300, coffee = 100, milk = 200, profit = 0.00)
espresso = Coffee(water = 100, coffee = 18, price = 1.50)
latte = Coffee(water = 200, coffee = 24, milk = 150, price = 2.50)
cappuccino = Coffee(water = 250, coffee = 24, milk = 100, price = 3.00)

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

def report():
    print(f"Resources Left:")
    print(f"Water: {tank.water}ml")
    print(f"Coffee: {tank.coffee}g")
    print(f"Milk: {tank.milk}ml")
    print(f"Profit: ${tank.profit:.2f}")

def payment():
    print("Please insert coins.")
    quarters = (float(input("How many quarters? "))) * 0.25
    dimes = (float(input("How many dimes? "))) * 0.10
    nickels = (float(input("How many nickels? "))) * 0.05
    pennies = (float(input("How many pennies? "))) * 0.01
    
    coins_inserted = quarters + dimes + nickels + pennies
    return round(coins_inserted, 2)

options = "/".join(menu.keys())
while True:
    order = input(
    f"What would you like? ({options})\n"
    "Type 'report' to see resources.\n"
    "Type 'off' to turn off the machine.\n").strip().lower()

    if order == "off":
        print("Turning off. Goodbye!")
        break

    elif order == "report":
        report()

    elif order in menu:
        drink = menu[order]

        # Check resources
        if tank.water < drink.water:
            print("Sorry there isn't enough water.")
        elif tank.coffee < drink.coffee:
            print("Sorry there isn't enough coffee.")
        elif tank.milk < drink.milk:
            print("Sorry there isn't enough milk.")
        else:
            # Process payment
            coins_inserted = payment()
            if coins_inserted < drink.price:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(coins_inserted - drink.price, 2)
                if change > 0:
                    print(f"Here's ${change} in change.")
                print(f"Here is your {order} ☕. Enjoy!")

                # Update tank
                tank.water -= drink.water
                tank.coffee -= drink.coffee
                tank.milk -= drink.milk
                tank.profit += drink.price
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
