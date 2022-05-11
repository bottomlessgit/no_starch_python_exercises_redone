pizza_flavors = ["pineapple", "raisin", "sardine", "blueberry"]
friend_pizza_flavors = pizza_flavors[:]
pizza_flavors.append("powdered sugar")
friend_pizza_flavors.append("chocolate syrup")
print("My favorite pizza flavors are:")
for flavor in pizza_flavors:
    print("\t" + flavor)
print("My friend's favorite pizza flavors are:")
for flavor in friend_pizza_flavors:
    print("\t" + flavor)
