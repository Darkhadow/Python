def ageChecker(birthYear):
    age = 2021 - int(birthYear)
    if int(birthYear) > 2021:
        print("No alphabets or symbols, only numbers are allowed")
    else:
        return(age)


import random
def mulitDice(numDice = 1, numSide = 6):
    print("\n      --Multi Dice Roller--")
    line = "-"*30
    dices = []
    input(f'''
Number of dices: {numDice}
Number of sides per dice: {numSide}
Press enter to roll...''')
    print(line)
    for dice in range(int(numDice)):
        dices.append(random.randint(1,int(numSide)))
    count = 1
    for dice in dices:
        print(f"Dice#{count}: {dice}")
        count += 1
    input(f'''
Total value: {sum(dices)}
{line}
Press enter to continue...''')
