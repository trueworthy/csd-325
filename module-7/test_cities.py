# Lea Trueworthy
# November 25, 2024
# CSD 325 - Module 7.2 Assignment: Test Cases
# Description: Create a function in city_functions.py that returns "City, Country".In test_cities.py, test the function using unittest.

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        # Test the function with city and country
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        # Test the function with city, country, and population
        result = city_country("Santiago", "Chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")

    def test_city_country_population_language(self):
        # Test the function with city, country, population, and language
        result = city_country("Santiago", "Chile", 5000000, "Spanish")
        self.assertEqual(result, "Santiago, Chile - population 5000000, Spanish")

if __name__ == "__main__":
    unittest.main()