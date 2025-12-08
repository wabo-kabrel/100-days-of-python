print("Welcome to Python Pizza Deliveries!")
size = input("What pizza size do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

S = 15
M = 20
L = 25

if (size.upper() == "S"):
    bill = S

elif (size.upper() == "M"):
    bill = M

elif (size.upper() == "L"):
    bill = L

else:
    print ("Invalid input, please try again!")


if (pepperoni.upper() == "Y"):
    bill += 2

if (extra_cheese.upper() == "Y"):
    bill += 1


print(f"Your total bill is ${bill}.")