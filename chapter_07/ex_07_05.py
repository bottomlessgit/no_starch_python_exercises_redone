message = "Tell me your age and I will tell your ticket price."
message += "Enter 'quit' to exit."
age = ""
while True:
    age = input("What is your age? ")

    if age.lower() == 'quit':
        print("Farewell!")
        break

    age = int(age)
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15

    print("Your ticket price is",str(price))