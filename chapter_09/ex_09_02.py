# Class taken from exercise 09_01 as instructed
class Restaurant():
    """Simple class that models a restaurant"""
    def  __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Prints message showing restaurant name and cuisine type"""
        print(self.restaurant_name.title() + " serves " + self.cuisine_type + ".")


    def open_restaurent(self):
        """Prints message that restaurant is open"""
        print(self.restaurant_name.title() + " is open.")


restaurant1 = Restaurant("mcdonalds", "fast food")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("saladtopia", "salad")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("medimagic", "mediterranean")
restaurant3.describe_restaurant()
