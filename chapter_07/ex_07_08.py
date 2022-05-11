sandwich_orders = ["tomato basil", "cheese plus", "blt", "tofu and beans"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("Your " + sandwich + "sandwich is finished. Enjoy!")
print("Sandiches Made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)