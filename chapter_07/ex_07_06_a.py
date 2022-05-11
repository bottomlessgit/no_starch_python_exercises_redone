# Code taken from ex_07_04 and altered to fit this exercise
# This code covers the choice of using a conditional test case
topping = ""
while topping != 'quit':
    topping = input("Input a desired pizza topping. Input 'quit' to exit. ")
    if topping == 'quit':
        print("Farewell!")
    else:
        print("We will add " + topping + " to your pizza.")
