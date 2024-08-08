from number_art import logo
import random

game_over = False

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
print(f"Psst!!. The number is {number}.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5


print(f"You have {attempts} attempts")

guess  = int(input("Make a guess:\n"))

def compare(guess, number):
    if guess > number:
        print("Too High")
    else:
        print("Too Low!")




while attempts > 0 and game_over == False:
    if guess == number:
        print(f"You guessed right!. The number is {number}")
        game_over = True
    else:
        compare(guess,number)
        attempts -= 1

        if attempts > 1:
            print(f"You have {attempts} attempts left.")
            guess  = int(input("Guess again:\n"))
        elif attempts == 1:
            print(f"You have {attempts} attempt left.")
            guess  = int(input("Guess again:\n"))

        if attempts <= 0:
            print("You've run out of guesses, you lose.")






