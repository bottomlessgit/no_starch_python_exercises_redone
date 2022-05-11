# Printing each line in file object with python replaced with C
with open("learning_python.txt") as file:
    for line in file:
        print(line.replace("python", "C").rstrip())