import random


class Die:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll_die(self):
        print(f"{random.randint(1,self.sides)}")


die1 = Die()
die1.roll_die()
die2 = Die(10)
die1.roll_die()

die3 = Die(20)
die3.roll_die()
