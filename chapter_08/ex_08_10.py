def show_magicians(magicians):
    """Prints a list of magician's titles in titlecase"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Takes a list of magician names and concatenates 
    'the great' at the beginning of each"""
    for magician in range(len(magicians)):
        magicians[magician] = "the great " + magicians[magician]

# Make list of magicians
magicians = [
    "the amazing raisin",
    "gary the clown",
    "chareth, the 'flirt'",
    "glinda the good witch",
    "bai su zhen, the healer"
    ]
# Use function to print them
print("Here are the magicians:")
show_magicians(magicians)

# Use make_great() function add 'the great' to each magician
make_great(magicians)
# Print again to show change
print("Here are the magicians made great:")
show_magicians(magicians)