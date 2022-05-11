# Printing result of .read() function
print("Using .read():")
with open("learning_python.txt") as file:
    print(file.read())

# Printing each line in file object
print("===\nUsing file object for-loop:")
with open("learning_python.txt") as file:
    for line in file:
        print(line.rstrip())

# Making list of lines using .readlines() function
print("===\nUsing .readlines():")
with open("learning_python.txt") as file:
    lines = file.readlines()

# Printing each line in readlines() result list
for line in lines:
    print(line.rstrip())

