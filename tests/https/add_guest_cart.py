import requests
import json

url = 'https://gmzungq13g.execute-api.us-east-1.amazonaws.com/default/add_to_cart_guest'
payload = {
    "items": [
        "3e310daa-d58a-45db-8a34-f5f1c75d36e8"
    ]
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
