numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
for number in numbers:
    print(str(number), end = "")
    if number > 2:
        print("th")
    elif number == 2:
        print("nd")
    else:
        print("st")