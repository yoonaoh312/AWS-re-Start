"""
Your module description
"""
print('welcome to guess the number!')
print('the rules are simple. i will think of a number, and you will try to guess it.')

import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input('guess a number between 1 and 10: ')
    if int(guess) == number:
        print('you guess {}. that is correct! you win'.format(guess))
        isGuessRight = True
    else:
        print('you guess {}. sorry that isn\'t it. try again'.format(guess) )
