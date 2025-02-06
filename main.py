# Import a library that allows to make HTTP request
import requests

# Set the API endpoint
url = "https://content-xflix-backend.azurewebsites.net/v1/videos/60331f421f1d093ab5424489"

# Use the library to perform an HTTP GET request to the URL
response = requests.get(url)

# Print out the data
print(response.text)