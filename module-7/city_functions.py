# Lea Trueworthy
# November 25, 2024
# CSD 325 - Module 7.2 Assignment: Test Cases
# Description: Create a function in city_functions.py that returns "City, Country".
    # Modify the function to include an optional population parameter, then make population optional.
    # Add an optional language parameter, then make it optional as well.
    # Run city_functions.py with all variations (city-country, city-country-population, and city-country-population-language).

def city_country(city, country):
    return(city, country)

print("Denver,", "United States")
print("Paris,", "France")
print("Santiago,", "Chile")

print(city_country("Denver", "United States"))