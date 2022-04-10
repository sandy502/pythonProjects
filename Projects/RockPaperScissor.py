# Rock Paper Scissors is a hand game originating from China, usually played between two people, 
# in which each player simultaneously forms one of three shapes with an outstretched hand. 
# These shapes are "rock", "paper", and "scissors". 
# well I have someone for you to play with.

import random

def play():
    user = input("*** (WARNING) Choose wisely or else you lose everything you have  ***\n\n . . . 'r' for ROCK, 'p' for PAPER and 's' for SCISSORS . . .\n")
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer:
        return 'It\'s a TIE. But you lost because you did not win. . .\n'

    if is_win(user, computer):
        return '\n You WON!!! we hope it happens again with you . . . :)'   

    return 'You LOST! Just because you take bad decisions not bad choices. . . :| \n'     

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True       

print(play())         