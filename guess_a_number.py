import random

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"Write a number between 1 and {x}: "))
        print(guess_number)
        
guess(10)
