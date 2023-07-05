import requests
import json

url = 'https://v2apssx6fb.execute-api.us-east-1.amazonaws.com/default/login_user'
payload = {
    'username': 'dikshant23',
    'password': 'passpass23',
    'cart': {
        "cart_id": "67902652-5bae-4961-8d6e-c65fafade557",
        "items": [
            1,
            2,
            3,
            4,
            5
        ],
        "total_price": 5000
    }
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
if response.status_code == 200:
    print(response.text)
    # data = response.json()
    # print('Response:', data)
    # Handle the response data here
else:
    print('Error:', response.text)
    # Handle any errors that occurred during the request
