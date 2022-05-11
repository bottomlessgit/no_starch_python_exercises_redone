""" What we want to do:
get the users favorite number:
    - If we have it then load it from the given json file.
    - If we don't, prompt the user for it.
        - The request of user input could trigger quit if invalid
announce the number to the user if we have it
"""

import json

def get_stored_number():
    """Returns stored number from json file or None if file absent"""
    try:
        with open("favorite_number_2.json") as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    # Finally return nuumber
    return favorite_number


def get_new_number():
    """Queries user for number, Or returns None if user entry invalid"""
    favorite_number_str = input("Please enter your favorite number: ")
    try:
        favorite_number = float(favorite_number_str)
    except ValueError:
        return None
    # Finally return number
    return favorite_number


def store_new_number(number):
    """Stores new number in json file"""
    with open("favorite_number_2.json", "w") as f_obj:
        json.dump(number, f_obj)


def tell_favorite_number():
    """Outputs message with favorite number if stored, if not
    queries user for new number and stores if valid input"""
    
    # First check to see if a number has been stored
    favorite_number = get_stored_number()
    if favorite_number:
        print("Your favorite number is " + str(favorite_number))
    else:
        # Query the 
        favorite_number = get_new_number()
        if favorite_number:
            store_new_number(favorite_number)
            print("Thank you, we will remember " + str(favorite_number)
                  + " is your favorite number.")
        else:
            print("Input was not a number, so no number was stored. Goodbye.")



tell_favorite_number()

