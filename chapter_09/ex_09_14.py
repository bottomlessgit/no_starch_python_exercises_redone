from random import randint

class Die():
    """Models a simple random n-sided die"""
    def __init__(self, num_sides):
        """Initializes the die object and it's number of sides"""
        if num_sides > 0:
            self.num_sides = num_sides
        else:
            print("Invalid number of sides. Creating standard 6-sided die.")
            self.num_sides = 6

    def roll_die(self):
        """Simulates die roll by returning random number between 1 and
        the number of sides."""
        return randint(1, self.num_sides)



print("Making a 6-sided and rolling die 10 times:")
six_sided = Die(6)
for num_roll in range(1, 11):
    print("roll " + str(num_roll) + ": " + str(six_sided.roll_die()))

print("\nMaking a 10-sided and rolling die 10 times:")
six_sided = Die(10)
for num_roll in range(1, 11):
    print("roll " + str(num_roll) + ": " + str(six_sided.roll_die()))

print("\nMaking a 20-sided and rolling die 10 times:")
six_sided = Die(20)
for num_roll in range(1, 11):
    print("roll " + str(num_roll) + ": " + str(six_sided.roll_die()))

