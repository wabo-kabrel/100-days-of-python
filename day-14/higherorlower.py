import game_data
import random

celeb_a_data = random.choice(game_data.game_data)
celeb_b_data = random.choice(game_data.game_data)

score = 0
right_choice = True

# Prevent celeb_a and celeb_b from being the same
while celeb_b_data == celeb_a_data:
    celeb_b_data = random.choice(game_data.game_data)

celeb_a = [celeb_a_data['name'], celeb_a_data['follower_count']]
celeb_b = [celeb_b_data['name'], celeb_b_data['follower_count']]


while right_choice:
    print(f"A: {celeb_a[0]} vs B: {celeb_b[0]}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()


    if user_choice == 'a':
        if celeb_a[1] > celeb_b[1]:
            print("Right! Next...")
            score+=1

            celeb_a = celeb_b
            new_celeb = random.choice(game_data.game_data)

            # Prevent duplicate comparison
            while new_celeb['name'] == celeb_a[0]:
                new_celeb = random.choice(game_data.game_data)

            celeb_b = [new_celeb['name'], new_celeb['follower_count']]

        else:
            print(f"Wrong! You lost with a score of {score}.")
            break

    elif user_choice == 'b':
        if celeb_b[1] > celeb_a[1]:
            print("Right! Next...")
            score +=1

            celeb_a = celeb_b
            new_celeb = random.choice(game_data.game_data)

            while new_celeb['name'] == celeb_a[0]:
                new_celeb = random.choice(game_data.game_data)

            celeb_b = [new_celeb['name'], new_celeb['follower_count']]

        else:
            print(f"Wrong! You lost with a score of {score}.")
            break

    else:
        print("Invalid input. Please type 'A' or 'B'.")