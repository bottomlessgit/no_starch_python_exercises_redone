def print_file(filename):
    """Prints contents of .txt file or catches exception  if file not found
    and sends error message without stopping program"""
    try:
        with open(filename) as file:
            print(file.read())
    except FileNotFoundError:
        print("Sorry, " + filename + " could not be found.")

# cats.txt file not included to exemplify succesful except block
print("Attempting to print cats.txt file contents")
print_file("cats.txt")

#dogs.txt is included and should print to console
print("\nAttempting to print dogs.txt file contents")
print_file("dogs.txt")