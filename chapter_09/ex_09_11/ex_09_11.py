# Demonstrates use of import of module with multiple classes
import user

# Code demonstrating instsantiation and use taken from ex_09_08 and altered
# Instance created to demonstrate functionality
admin_privileges = ["alter user profiles", "post updates", "delete posts"]
privileges = user.Privileges(admin_privileges)
admin1 = user.Admin("vermin", "supreme", "vsauce", "06/06/1960", True, 
               privileges, "01/01/2050")

# First call method from admin class to show functionality remains
admin1.show_privileges()

# Call again but now straight from Privilege class attribute
admin1.privileges.show_privileges()