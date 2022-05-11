class Restaurant():
    """Simple class that models a restaurant"""
    def  __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Prints message showing restaurant name and cuisine type"""
        print(self.restaurant_name.title() 
              + " serves " 
              + self.cuisine_type 
              + ".")


    def open_restaurent(self):
        """Prints message that restaurant is open"""
        print(self.restaurant_name.title() + " is open.")


    def set_number_served(self, number_served):
        """Sets the number_served attribute to a given value"""
        # Check for invlid negative value
        if number_served < self.number_served:
            print("You can't serve a negative number of people!")
        else:
            self.number_served = number_served


    def increment_number_served(self, newly_served):
        """Increments the number_served attribute by a given value"""
        # Check for invlid negative value
        if newly_served < 0:
            print("You can't serve a negative number of people!")
        else:
            self.number_served += newly_served


    # Method added to assist with sample instance output
    def announce_number_served(self):
        print("The restaurant has now served " 
              + str(self.number_served)
              + " customers.")


# Show initial number_served value
restaurant1 = Restaurant("ihop", "american breakfast cuisine")
restaurant1.announce_number_served()

# Change number_served using set_number_served method
new_number_served = 1234
restaurant1.set_number_served(new_number_served)
restaurant1.announce_number_served()

# Demonstrate set_number_served protection against illegal decrease
new_number_served =  1000
print("We will attempt to change number served to a lower value of " 
      + str(new_number_served))
restaurant1.set_number_served(new_number_served)

# Change number_served using increment_number_served method
newly_served_increment = 55
print("We will add " + str(newly_served_increment) + " customers to the count.")
restaurant1.increment_number_served(newly_served_increment)
restaurant1.announce_number_served()

# Demonstrate set_number_served protection against illegal decrease
newly_served_increment =  -20
print("We will attempt to change number served by an illegal negative value of " 
      + str(newly_served_increment))
restaurant1.increment_number_served(newly_served_increment)




