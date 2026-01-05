# LOCAL SCOPE
# Variables declared inside a function have local scope.
# They are only accessible within that function.

def drink_potion():
    potion_strength = 2  # Local variable
    print(potion_strength)

drink_potion()


# GLOBAL SCOPE
# Global variables are defined outside of functions, usually at the top of the file.
# They can be accessed (read) both inside and outside functions.

player_health = 10  # Global variable

def show_health():
    print(player_health)  # Accessing global variable

show_health()
print(player_health)


# MODIFYING GLOBAL VARIABLES
# By default, global variables cannot be modified inside a function.
# The "global" keyword allows a function to modify a global variable.
# NOTE: Using "global" is generally discouraged in large programs because
# it can make code harder to debug and maintain.

enemies = 1  # Global variable

def increase_enemies():
    global enemies
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
