import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")

letters_length = int(input("How many letters would you want your password to have?\n"))
numbers_length = int(input("How many number would you want your password to have?\n"))
symbols_length = int(input ("How many symbols would you want your password to have?\n"))

# Easy version: Generate the password in sequence. Letters, then symbols, then numbers.

'''
password = ""

for x in range(0, letters_length):
    password = password + random.choice(letters)

for y in range(0, numbers_length):
    password = password + random.choice(numbers)

for z in range(0, symbols_length):
    password = password + random.choice(symbols)

print(f"Your password is {password}")
'''

# Hard level: Generate a completely random password which doesn't follow any sequence or pattern.

password_list = []

for x in range(0, letters_length):
    password_list.append(random.choice(letters))

for y in range(0, numbers_length):
    password_list.append(random.choice(numbers))

for z in range(0, symbols_length):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i

print(f"Your generated password is {password}")