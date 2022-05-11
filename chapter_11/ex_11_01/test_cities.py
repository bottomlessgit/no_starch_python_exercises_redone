import unittest
from city_functions import get_location_name


class LocationTestCase(unittest.TestCase):
    """Tests for get_location_name function from city_functions module"""

    def test_city_country(self):
        """Do loccations like 'Santiago, Chile' work?"""
        location_name = get_location_name("santiago", "chile")
        self.assertEqual("Santiago, Chile", location_name)

unittest.main()