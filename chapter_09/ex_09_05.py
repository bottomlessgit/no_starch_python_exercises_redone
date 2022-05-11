# User class taken from execise 09_03 as instructed
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
        # login_attempts attribute added for execise 09_05
        self.login_attempts = 0
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


    def increment_login_attempts(self):
        """Increments login_attempts attribute by 1"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Resets login_attempts to 0"""
        self.login_attempts = 0


# Now creating instance and tracking login attempts to test functionality
user1 = User("jane", "doe", "johndorian4ever", "08/12/1990", False)
print(user1.login_attempts)
# Now increment login attempts 7 times as instructed
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
# Print value to check it has been incrememnted successfully
print(user1.login_attempts)
# Now test reset_login_attempts fucntion and print attribute
user1.reset_login_attempts()
print(user1.login_attempts)

