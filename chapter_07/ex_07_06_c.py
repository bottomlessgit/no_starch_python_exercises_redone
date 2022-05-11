# Code taken from ex_07_04 and altered to fit this exercise
# This code covers the choice of using an 'active' flag break statement
while True:
    topping = input("Input a desired pizza topping. Input 'quit' to exit. ")
    if topping == 'quit':
        print("Farewell!")
        break
    else:
        print("We will add " + topping + " to your pizza.")
