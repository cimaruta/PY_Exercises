from random import randint

class Dice:

    def __init__(self, sides=6):
        self.sides = sides


    def roll_dice(self):
        dice_roll = randint(1, self.sides)
        rolls.append(dice_roll)

d6 = Dice()

rolls = []

while len(rolls) < 10:
    d6.roll_dice()

print(rolls)

d10 = Dice(10)

rolls = []

while len(rolls) < 10:
    d10.roll_dice()

print(rolls)