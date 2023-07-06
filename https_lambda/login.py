

import requests

LOGIN_ENDPOINT = "https://v2apssx6fb.execute-api.us-east-1.amazonaws.com/default/login_user"

input = {
    "username": "dikshant",
    "password": "pass",
    "cart_id": "37a58683-5ac2-4a40-9334-77a6e12ea50a"
}

# response = requests.post(LOGIN_ENDPOINT, json=input)
output = {"msg": "Login Sucess",
          "user_id": "9a8757fa-ea37-47d2-baf7-62e5ae1236f3",
          "name": "Dikshant Naik"}


# print(response.text)
