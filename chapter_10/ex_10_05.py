# I opened the file in append mode as an example
with open("programmer_poll.txt", "a") as poll:
    print("This is a poll of why people like programming. Enter 'q' to quit")
    while True:
        response = input("Why do you like programming?\n")
        if response == 'q':
            print("Farewell!")
            break
        else:
            poll.write(response + "\n")
            print("Thank you for your response!\n")