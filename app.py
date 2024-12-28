# Project:2 Guess the number (Computer)
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. to low.")
        elif guess > random_number:
            print("Sorry, guess again. to high")    

    print(f"Congrats, you guessed the number {random_number} correctly!")

guess(10)