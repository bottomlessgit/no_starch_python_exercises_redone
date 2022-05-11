# Privileges class taken from ex_09_08

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