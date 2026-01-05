import random

correct_guess = False

def play_game():
    attempts = 0
    print("""Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.""")

    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid choice.")
        return False

    while attempts > 0:       
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You guessed the correct number, {guess}.")
            return True

        else:
            diff = guess - number

            if diff > 30:
                print("Too high.")
            elif diff < -30:
                print("Too low.")
            elif diff > 15:
                print("High.")
            elif diff < -15:
                print("Low.")
            else:
                print("Almost there")

            attempts -= 1

    print(f"0 attempts left. The number was {number}.")
    return False

play_game()
