"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

def title():
    print("Tutorial: use WASD to move, space to jump, left click to attack, right click to interact.")
    print("Just kidding. Try to guess the number.")
def game():
    import random
    x = random.randint(1,10)
    attempts = 0
    y = 0
    while x != y:
        y = int(input("\nPick a number from 1 to 10: "))
        attempts = attempts + 1
    else:
        print(f"You guessed the number right, it took you {attempts} attempt(s)")

title()
game()
