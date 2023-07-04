import requests
import json

url = 'https://a0aq2g3pdh.execute-api.us-east-1.amazonaws.com/default/add_product_2'
payload = {
    'product_id': 'awdawdawd',
    'product_name': 'Banana',
    'product_price': 500,
    'product_category': 'fruit'
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
