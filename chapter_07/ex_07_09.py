sandwich_orders = ["pastrami", "tomato basil", "pastrami", "cheese plus", "blt", "tofu and beans", "pastrami"]
finished_sandwiches = []
print("We're out of pastrami, sorry.\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("Your " + sandwich + "sandwich is finished. Enjoy!")
print("Sandiches Made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)