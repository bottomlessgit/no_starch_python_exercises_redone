# Demonstrates import of classes to other modules
from restaurant import Restaurant
# Code taken from ex_09_01
my_restaurant = Restaurant("gusteau's", "italian cuisine")
# Print attributes without methods
print("restaurant_name attribute's value is: " + my_restaurant.restaurant_name)
print("cuisine_type attribute's value is: " + my_restaurant.cuisine_type + "\n")
# Now use methods
my_restaurant.describe_restaurant()
my_restaurant.open_restaurent()