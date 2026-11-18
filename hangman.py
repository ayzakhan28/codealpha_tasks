
import random

hang_list = ["HANGMAN", "COMPUTER", "PYTHON", "PROJECT", "PROGRAMME"]

stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

secret_word = random.choice(hang_list)

guessed_letter = set()
wrong_letter = 0

print("Welcome to Hangman Game!")
print(stages[wrong_letter])

while wrong_letter < 6:

    guess = input("\nEnter a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
       print("Please enter only one alphabet!")
       continue


    # Check duplicate guess
    if guess in guessed_letter:
        print("You already guessed this letter!")
        continue

    guessed_letter.add(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print("Correct Guess!")
    else:
        print("Wrong Guess!")
        wrong_letter += 1

    # Display Hangman drawing
    print(stages[wrong_letter])

    # Display guessed word
    for letter in secret_word:
        if letter in guessed_letter:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    # Check winning condition
    if all(letter in guessed_letter for letter in secret_word):
        print("\nCongratulations! You Win!")
        break

# Losing condition
if wrong_letter == 6:
    print("\nGame Over!")
    print("The secret word was:", secret_word)
