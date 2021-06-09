from random import randint


class Die():
    """ Simulates the roll of a single die """

    def __init__(self, num_sides: int = 6) -> None:
        self.num_sides = num_sides

    def roll(self) -> int:
        return randint(1, self.num_sides)
