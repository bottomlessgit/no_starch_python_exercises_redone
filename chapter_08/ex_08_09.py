def show_magicians(magicians):
    """Prints a list of magician's titles in titlecase"""
    for magician in magicians:
        print(magician.title())

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