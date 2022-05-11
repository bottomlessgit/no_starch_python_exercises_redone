class User():
    """Simple class to represent user of application"""
    def __init__(self, first_name, last_name, username, date_of_birth, 
                 is_plus_member, membership_expiration_date = ""):
        """Initializes user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth
        self.is_plus_member = is_plus_member
        if membership_expiration_date:
            self.membership_expiration_date = membership_expiration_date


    def describe_user(self):
        """Prints all user attribute information"""
        print("Username: " + self.username)
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Date of Birth: " + self.date_of_birth)
        if self.is_plus_member:
            print("Your plus membership expires on " 
                  + self.membership_expiration_date)


    def greet_user(self):
        """Short personalized memebership-dependent user greeting"""
        if self.is_plus_member:
            print("Hello " + self.first_name.title() 
                  + " " + self.last_name.title()
                  + ", our esteemed guest, welcome back to our humble app")
        else:
            print("Oh hey " + self.first_name.title() + ", you're here. Hi.")


user1 = User("jane", "doe", "johndorian4ever", "08/12/1990", False)
user1.greet_user()
user1.describe_user()
print("\n\n")
user2 = User("scrooge", "mcduck", "olympicgoldswimmer", "12/13/1947", True 
             , "11/10/2043")
user2.greet_user()
user2.describe_user()

