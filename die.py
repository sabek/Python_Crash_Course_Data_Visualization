from random import randint


class Die():
    """"A Class representing Dice"""

    def __init__(self, num_sides=6):
        """Assume 6 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """"Roll a random number from 1 to num_sides"""
        return randint(1, self.num_sides)
