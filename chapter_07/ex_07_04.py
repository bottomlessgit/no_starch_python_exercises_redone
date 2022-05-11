topping = ""
while topping != 'quit':
    topping = input("Input a desired pizza topping. Input 'quit' to exit. ")
    if topping != 'quit':
        print("We will add " + topping + " to your pizza.")
    else:
        print("Farewell!")