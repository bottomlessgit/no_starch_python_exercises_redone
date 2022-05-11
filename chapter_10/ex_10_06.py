print("We are going to add 2 integers of your choosing.")
input1 = input("Please input the first integer: ")
input2 = input("Please input the second integer: ")
# Variable to check whether input threw errors before adding
input_valid = True

try:
    num1 = int(input1)
except ValueError:
    print("Sorry, " + input1 + " is not a valid integer.")
    input_valid = False

try:
    num2 = int(input2)
except ValueError:
    print("Sorry, " + input2 + " is not a valid integer.")
    input_valid = False

if input_valid:
    result = num1 + num2
    print("The sum of your inputs is: " + str(result))
