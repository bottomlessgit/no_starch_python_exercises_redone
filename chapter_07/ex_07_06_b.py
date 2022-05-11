# Code taken from ex_07_04 and altered to fit this exercise
# This code covers the choice of using an 'active' flag
active = True
while active:
    topping = input("Input a desired pizza topping. Input 'quit' to exit. ")
    if topping == 'quit':
        active = False
        print("Farewell!")
    else:
        print("We will add " + topping + " to your pizza.")
