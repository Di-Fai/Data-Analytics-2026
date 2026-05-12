# Description: This is a simple number guessing game
# Author: Dimitri Nji

from datetime import datetime

# Create the range of numbers
numbers = list(range(1, 21))

# Create a set from the list to show a second collection type
number_set = set(numbers)

# Use the current time to help pick a number without using the random module
time_number = datetime.now().microsecond

# Use the time number to choose a position from the list
secret_number = numbers[time_number % len(numbers)]

guesses = []
guess_count = 0

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 20.")
print("Try to guess the number.")
print()

while True:
    user_input = input("Enter your guess: ")

    if not user_input.isdigit():
        print("Please enter a number only.")
        continue

    guess = int(user_input)
    guesses.append(guess)
    guess_count = guess_count + 1

    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print()
        print("Correct! You guessed the number.")
        print("Number of guesses:", guess_count)
        print("Your guesses:", guesses)

        if guess_count < 5:
            print("You are awesome!")

        break

'''
This program creates a guessing game where the computer picks a number between 1 and 20.
The user keeps guessing until they get the correct answer. 
If the guess is too low, the program says “Higher.” 
If the guess is too high, it says “Lower.” The program also counts the guesses, 
saves all guessed numbers, and handles mistakes if the user types something that is not a number.
'''
    