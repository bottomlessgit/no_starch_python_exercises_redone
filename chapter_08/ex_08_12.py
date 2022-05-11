def make_sandwich(*fillings):
    """Accepts arbitrary number of sandwich fillings and prints out 
    a description of the resulting sandwich"""
    print("Your sandwich has fillings of:")
    for filling in fillings:
        print("\t-" + filling)

# Call function on different number of arguments to demonstrate function
make_sandwich("mayo", "lettuce", "bacon")
make_sandwich("mustard", "mayo", "ketchup", "pickles", "peanut butter")
make_sandwich("mozarella cheese")