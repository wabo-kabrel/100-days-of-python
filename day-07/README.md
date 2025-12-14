# Hangman Game in Python

A simple **console-based Hangman game** written in Python. The game picks a random word from a predefined list, and the player has to guess the letters before running out of lives. The game also displays a simple ASCII Hangman for each wrong guess.

---

## Features

- Randomly selects a word from a small word list: `["candy", "pay", "book", "touch"]`.
- Shows underscores `_` for letters to be guessed.
- Tracks the number of lives (6 by default).
- Displays **ASCII Hangman stages** as the player makes wrong guesses.
- Case-insensitive letter input.
- Prints a congratulatory message if the player guesses the word.
- Shows the full word and Hangman if the player loses.

---

## How to Play

1. Run the Python script:
   ```bash
   python hangman.py
The program displays the word as underscores _.

Type a single letter as your guess.

If the letter is in the word, it will replace the corresponding underscore(s).

If the letter is not in the word, you lose one life, and the Hangman ASCII art updates.

Keep guessing until you either guess the word correctly or run out of lives.

Example
less
Copy code
_ _ _ _ _
Guess a letter:
> a
_ a _ _ _
Requirements
Python 3.x

No external libraries required

Notes
The word list is small; you can expand it by adding more words to the words list.

The ASCII Hangman stages can be customized for different visual styles.

Enjoy the game!