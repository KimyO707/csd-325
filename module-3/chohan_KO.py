"""Cho-Han, Modified by Kimberly Orozco
Original by Al Sweigart al@inventwithpython.com
Assignment: Brownfield + Flowchart
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, Modified by Kimberly Orozco

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS RULE: If your roll equals 2 or 7, you earn a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('ko: ')  # KIMBERLY: Changed input prompt to initials
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)# Convert pot to an integer.
            break# Exit the loop once a valid bet is placed.

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('ko: ').upper() # KIMBERLY: Changed input prompt to initials
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    #KIMBERLY: Added total variable to reuse for the 2 or 7 bonus check.
    total = dice1 + dice2
    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = (bet == correctBet)

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        fee = int(pot * 0.12)  #KIMBERLY: Changed house fee to 12%
        print('The house collects a', fee, 'mon fee.')
        purse -= fee
    else:
        purse -= pot
        print('You lost!')

    #KIMBERLY: Bonus for roll of 2 or 7 ONLY IF the player wins ;)
    #I want to add that it took me so long to test if this part really works. 
    #The trick is to only bet on HAN till you get a 7, since it's more likely to happen.
    if playerWon:
        if total == 2 or total == 7:
            print(f'Lucky roll! The total was {total}, so you get a 10 mon bonus!')
            purse += 10

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()