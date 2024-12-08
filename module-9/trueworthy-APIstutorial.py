# Lea Trueworthy
# December 6, 2024
# CSD 325 - Module 9.2 Assignment: API [tutorial]
# Description: https://www.dataquest.io/blog/api-in-python/
# Create a Python program for the tutorial to test the connection, fetch the current astronauts, and format the output

# Import the requests
import requests

# Import the json library
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Make a GET request to the Open Notify API for a list of astronauts currently in space
response = requests.get('http://api.open-notify.org/astros.json')

# Print the status code of the response
print(response.status_code)

# print response in a readable format
jprint(response.json())