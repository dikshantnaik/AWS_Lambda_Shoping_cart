import requests
import json

url = 'https://v2apssx6fb.execute-api.us-east-1.amazonaws.com/default/login_user'
payload = {
    'username': 'dikshant23',
    'password': 'passpass23',
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.text)
if response.status_code == 200:
    data = response.json()
    print('Response:', data)
    # Handle the response data here
else:
    print('Error:', response.text)
    # Handle any errors that occurred during the request
