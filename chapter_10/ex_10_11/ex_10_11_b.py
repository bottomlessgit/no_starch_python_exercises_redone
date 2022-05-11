import json

try:
    filename = "favorite_number.json"
    with open(filename) as file:
        favorite_number = json.load(file)
        print("I know your favorite number! It's " + str(favorite_number))
except FileNotFoundError:
    print("Your favorite number has not been recorded.")