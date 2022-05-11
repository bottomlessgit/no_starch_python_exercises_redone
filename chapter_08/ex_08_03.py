def make_shirt(size, text):
    """Prints a message about shirt size and the text that covers it"""
    shirt_message = ("The size of the shirt is {size},"
                     " the text contained is {text}.")
    print(shirt_message.format(size = size, text = text))

# Set example values
shirt_size = "M"
shirt_text = "My other shirt is a Ferrari"

# First call function with positional arguments
make_shirt(shirt_size, shirt_text)

# Then call function with keyword arguments
make_shirt(text = shirt_text, size = shirt_size)