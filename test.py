import requests

# Define the API endpoint URL
api_url = 'http://localhost:5000/get_course_details'

# Define the JSON payload with your username and password
data = {
    'username': 'e21cseu0428',
    'password': '8Sm&5Xl&'
}

# Make the POST request
response = requests.post(api_url, json=data)

# Check the response
if response.status_code == 200:
    course_details = response.json()
    print(course_details)
else:
    print('Error:', response.status_code)
