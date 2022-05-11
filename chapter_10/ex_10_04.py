# Safely open guestbook file to write to
with open("guest_book.txt", "w") as guest_book:
    # Explain game to users
    print("Guests should enter their names. If you'd like to quit, enter 'q'.")
    response = ""
    while True:
        # Ask user for input
        response = input("What is your name? ")
        # If user inputs 'q' say goodbye and exit
        if response == "q":
            print("Farewell!")
            break
        else:
            print("Thank you for answering " + response + "!")
            guest_book.write(response + "\n")
