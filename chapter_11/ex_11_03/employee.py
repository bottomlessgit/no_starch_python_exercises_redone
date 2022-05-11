# This class will be used to demonstrate the use of the unittest module
class Employee():
    """Simple attempt to model an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Initializes employee name and salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary


    def give_raise(self, salary_raise=5000):
        """increases annual_salary attribute by salary_raise"""
        self.annual_salary += salary_raise