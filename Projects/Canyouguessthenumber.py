#here computer generates random numbers using random library and we have to guess it correctly.

import random
def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input(f'\nguess a number between 1 to {x}: '))
        if guess < number:
            print("\nSorry, It was low. Looks like you have too low standards !!!\n")
        elif guess > number:
            print("\nSorry, guess again. Your high standards doesn't match ours!!!\n")

    print("\nSurprise! Surprise!! mf!!! You just hit the jackpot!!!\n")
    print(f'\ncongrats!!! you are  idiot number {number} in our list.')        

guess(10)            
