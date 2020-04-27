# Debug coin toss
# project has several bugs, need to solve them

import random

guess = ''
while guess not in ('heads' , 'tails'):
    print('Guess the coin toss! Enter heads or tails')
    guess = input()
    # Coin toss guess was defined as a string, need to change to int
if guess == 'heads':
    guess = 1
else:
    guess = 0
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input() # Variable was misspelled was guesss
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    if toss == guess:
        print('You got it')
    else: print('Nope. You are really bad at this game.')
