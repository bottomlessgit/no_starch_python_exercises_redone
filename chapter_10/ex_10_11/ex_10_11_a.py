import json

# First prompt user for number and make sure number is valid
favorite_number = input("Please enter your favorite number: ")
try:
    favorite_number = float(favorite_number)
except ValueError:
    print("That is not a valid number. No number recorded. Goodbye.")
else:
    filename = "favorite_number.json"
    with open(filename, "w") as file:
        json.dump(favorite_number, file)