#here we generate random number and computer guesses correctly.

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    
        feedback = input(f'Is {guess} too high (h) or too low (l) or correct (c) ???').lower()
        if feedback == 'h':
            print('\nYe sab Doglapan hai. (You hipocrite !!!)...\n')
            high = guess - 1
        elif feedback == 'l':
            print('\nBhai kya kar raha/rahi hai tu!!! Aisa kaise chalega!!! (Bro what are you doing!!! )\n\n')
            low = guess + 1

    print(f'\nComputer guessed the number {guess} correctly!!!' )
    print('\nBillkul bakwas tha ye!!!')            

x = int(input("\nYOU FREAKY HUMAN!!! TELL ME UPTO WHICH HIGHER RANGE OF NUMBER SHOULD I GUESS ?\n"))
computer_guess(x)    