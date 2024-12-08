# https://www.dataquest.io/blog/api-in-python/

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