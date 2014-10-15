'''
Rules of play

Each casino may set which bets are offered and different payouts for them,
though a core set of bets and payouts is typical. Players take turns rolling two
dice and whoever is throwing the dice is called the "shooter".  Players can bet
on the various options by placing chips directly on the appropriately-marked
sections of the layout, or asking the base dealer or stickman to do so,
depending on which bet is being made.

While acting as the shooter, a player must have a bet on the "Pass" line or the
"Don't Pass" line. "Pass" and "don’t pass" are sometimes called "Win" and "Don’t
Win" or "Right" and "Wrong" bets. The game is played in rounds and these "Pass"
and "Don't Pass" bets are betting on the outcome of a round. The shooter is
presented with multiple dice (typically five) by the "stickman", and must choose
two for the round. The remaining dice are returned to the stickman's bowl and
are not used.

Each round has two phases: "come-out" and "point". To start a round, the shooter
makes one or more "come-out" rolls. A come-out roll of 2, 3 or 12 is called
"craps" or "crapping out", and anyone betting the Pass line loses. A come-out
roll of 7 or 11 is a "natural", and the Pass line wins. The other possible
numbers are the point numbers: 4, 5, 6, 8, 9, and 10. If the shooter rolls one
of these numbers on the come-out roll, this establishes the "point" - to "pass"
or "win", the point number must be rolled again before a seven. The dealer flips
a button to the "On" side and moves it to the point number signifying the second
phase of the round. If the shooter "hits" the point value again (any value of
the dice that sum to the point will do; the shooter doesn't have to exactly
repeat the value combination of the come-out roll) before rolling a seven, the
Pass line wins and a new round starts. If the shooter rolls any seven before
repeating the point number (a "seven-out"), the Pass line loses and the dice
pass clockwise to the next new shooter for the next round. In all the above
scenarios, whenever the Pass line wins, the Don't Pass line loses, and vice
versa, with one exception: on the come-out roll, a roll of 12 will cause Pass
Line bets to lose, but Don't Pass bets are pushed (or "barred"), neither winning
nor losing. (The same applies to "Come" and "Don't Come" bets, discussed below.)

From http://en.wikipedia.org/wiki/Craps
'''
from random import randint

# this is the come-out roll
print('come-out')
r1 = randint(1, 6)
r2 = randint(1, 6)
v = r1 + r2
# display the come-out roll
print(v)
# if the come-out roll is a 7 or an 11, the player wins.
if v == 7 or v == 11:
    print('You win!')
# if the come-out roll is a 2, 3, or 12, the player loses
elif v == 2 or v == 3 or v == 12:
    print('Craps, you lose.')
# otherwise the come-out roll becomes the "point"
else:
    print('The point is', v)
    # roll the dice
    r1 = randint(1, 6)
    r2 = randint(1, 6)
    w = r1 + r2
    # print the roll
    print(w)
    # keep rolling until the point is rolled or a 7 is rolled
    while w != v and w != 7:
        r1 = randint(1, 6)
        r2 = randint(1, 6)
        w = r1 + r2
        print(w)
    # if a 7 is rolled before the point, the player loses
    if w == 7:
        print('Seven out, you lose.')
    # if the point was rolled before a 7, the player wins!
    else:
        print('Pass, you win!')
