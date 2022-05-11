import unittest
from employee import Employee

class test_employee(unittest.TestCase):
    """Class to test methods of Employee class"""

    def setUp(self):
        """creates an instance of the Employee class for tests to use"""
        self.my_employee = Employee("Worky", "McWorkerson", 50000)
        self.my_raise = 10000


    def test_give_default_raise(self):
        """Tests give_raise method with default raise"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 55000)


    def test_give_custom_raise(self):
        """Tests give_raise method with custom raise"""
        self.my_employee.give_raise(self.my_raise)
        self.assertEqual(self.my_employee.annual_salary, 60000)

unittest.main()