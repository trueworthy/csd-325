# Lea Trueworthy
# December 6, 2024
# CSD 325 - Module 9.2 Assignment: APIs
# Description: https://pokeapi.co/docs/v2#machines-section
# Create a Python program that will test the connection, retrieve data about a specific Pokdmon machine, and format the output

# Import the requests
import requests

# Import the json library
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Send a GET request to the PokeAPI endpoint to retrieve machine data for machine ID 2
response = requests.get('https://pokeapi.co/api/v2/machine/2')

# Print the status code of the response
print(response.status_code)

# print response in a readable format
jprint(response.json())