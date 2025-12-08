import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to the Rock-Paper-Scissors Game.")

try:
    user_choice = int(input("Enter 0 to choose Rock, 1 to choose Paper, and 2 to choose Scissors.\n"))
    computer_choice = random.randint(0,2)

    if (user_choice >= 3) or (user_choice < 0):
        print("You made an invalid choice. You lose!")

    else:
        print(f"You chose: \n{game_images[user_choice]}")
        print(f"Computer chose: \n{game_images[computer_choice]}")

        if (user_choice == computer_choice):
            print("It's a draw!")

        elif (user_choice == 0) and (computer_choice == 2):
            print("You win!")

        elif (user_choice == 2) and (computer_choice == 0):
            print("You lose!")

        elif (user_choice > computer_choice):
            print("You win!")

        elif (user_choice < computer_choice):
            print("You lose")

except ValueError:
    print("Invalid choice. Please choose 0 for rock, 1 for paper or 2 for scissors.")

    