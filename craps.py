'''
Rules of play

From http://en.secondTotalikipedia.org/secondTotaliki/Craps
'''
from random import randint

print('come-out')
roll1 = randint(1, 6)
roll2 = randint(1, 6)
firstTotal = roll1 + roll2
print(firstTotal)

if firstTotal == 7 or firstTotal == 11:
    print('You win!')

elif firstTotal == 2 or firstTotal == 3 or firstTotal == 12:
    print('Craps, you lose.')

else:
    print('The point is', firstTotal)
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    secondTotal = roll1 + roll2
    print(secondTotal)
    
    while secondTotal != firstTotal and secondTotal != 7:
        roll1 = randint(1, 6)
        roll2 = randint(1, 6)
        secondTotal = roll1 + roll2
        print(secondTotal)
        
    if secondTotal == 7:
        print('Seven out, you lose.')
        
    else:
        print('Pass, you win!')
