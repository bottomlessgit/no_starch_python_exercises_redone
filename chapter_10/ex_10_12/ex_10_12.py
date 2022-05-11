import json

filename = "favorite_number.json"
try:
    with open(filename) as f_obj:
        favorite_number_str = json.load(f_obj)
        print("I know your favorite number! It's " + str(favorite_number_str))
except FileNotFoundError:
    # If file doesn't exist prompt user for favorite number
    favorite_number_str = input("Please input your favorite number: ")
    try:
        favorite_number = float(favorite_number_str)
        with open(filename, "w") as f_obj:
            json.dump(favorite_number, f_obj)
        print("Thanks, we will remember that.")
    except ValueError:
        # If value entered is not valid number announce it and end program
        print(favorite_number_str + " is not a valid number. Goodbye.")
