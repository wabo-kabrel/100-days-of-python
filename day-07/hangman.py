import random 

print("""
_    _          _   _     _  __    _  
 | |  | |        | | | |   | |/ /   | | 
 | |__| | __ _  _| |_| |__ | ' / ___| | 
 |  __  |/ _` || | __| '_ \|  < / _ \ | 
 | |  | | (_| || | |_| | | | . \  __/_| 
 |_|  |_|\__,_||_|\__|_| |_|_|\_\___(_)
""")
lives = 6

words = ["candy", "pay", "book", "touch"]
word = random.choice(words)

blanks = []

for letter in word:
    blanks.append("_")

blanks_string = "".join(blanks)
print(f"Word: {blanks_string}")

hangman_stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

while ((lives > 0) and ("_" in blanks)):
    guess = input("Guess a letter you think is in the word: ").lower()

    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                blanks[i] = guess
    else:
        lives = lives - 1
        print(f"Wrong guess! Lives left: {lives}")
        print(hangman_stages[6-lives])

    blanks_string = "".join(blanks)
    print(blanks_string)

if "_" not in blanks_string:
    print(f"Congratulations! You guessed the word: {word}")

else:
    print(f"Game over! The word was: {word}")
