# Class taken from ex 09_01 as instructed
class Restaurant():
    """Simple class that models a restaurant"""
    def  __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Prints message showing restaurant name and cuisine type"""
        print(self.restaurant_name.title() + " serves " 
              + self.cuisine_type + ".")


    def open_restaurent(self):
        """Prints message that restaurant is open"""
        print(self.restaurant_name.title() + " is open.")


class IceCreamStand(Restaurant):
    """Class extends Restaurant to model an ice cream stand with flavors"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initializes restaurant attributes and list of flavors"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


    def list_flavors(self):
        """Lists flavors offered by this stand"""
        print(self.restaurant_name.title() + " has the following flavors:")
        for flavor in self.flavors:
            print("\t-" + flavor)


# Instance created to demonstrate functionality
flavors = ["chocolate", "vanilla", "strawberry", "caramel", "cookie dough"]
ice_cream_stand1 = IceCreamStand("stand and jerry's", "boutique ice cream", 
                                 flavors)
# Call subclass method
ice_cream_stand1.list_flavors()