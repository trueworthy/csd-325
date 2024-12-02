# Lea Trueworthy
# November 25, 2024
# CSD 325 - Module 7.2 Assignment: Test Cases
# Description: Create a function in city_functions.py that returns "City, Country".
    # Modify the function to include an optional population parameter, then make population optional.
    # Add an optional language parameter, then make it optional as well.
    # Run city_functions.py with all variations (city-country, city-country-population, and city-country-population-language).

def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"

# Calling the function with different parameters
print(city_country("Denver", "United States"))
print(city_country("Paris", "France", 2200000))
print(city_country("Santiago", "Chile", 5000000, "Spanish"))