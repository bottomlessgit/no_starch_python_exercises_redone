# User Superclass taken from ex_09_03 as instructed
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


class Admin(User):
    """Class to extend user class for aministrative user"""
    def __init__(self, first_name, last_name, username, date_of_birth, 
                 is_plus_member, privileges, membership_expiration_date = ""):
        """Initializes user attributes and privileges list"""
        super().__init__(first_name, last_name, username, date_of_birth, 
                         is_plus_member, membership_expiration_date)
        self.privileges = privileges


    # Function to call Privilege class show_privileges method from Admin
    def show_privileges(self):
        self.privileges.show_privileges()


# New privilege class to handle privilege list
class Privileges():
    """Class that contains and can list user privileges"""
    def __init__(self, privilege_list):
        """Initializes list of privileges"""
        self.privileges = privilege_list

    def show_privileges(self):
        """Prints list of privileges"""
        print("Privileges:")
        for privilege in self.privileges:
            print("\t-" + privilege)

# Instance created to demonstrate functionality
admin_privileges = ["alter user profiles", "post updates", "delete posts"]
privileges = Privileges(admin_privileges)
admin1 = Admin("vermin", "supreme", "vsauce", "06/06/1960", True, 
               privileges, "01/01/2050")

# First call method from admin class to show functionality remains
admin1.show_privileges()

# Call again but now straight from Privilege class attribute
admin1.privileges.show_privileges()



