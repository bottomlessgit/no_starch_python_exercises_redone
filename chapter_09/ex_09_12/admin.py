# Admin class taken from ex_09_08
import user

class Admin(user.User):
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