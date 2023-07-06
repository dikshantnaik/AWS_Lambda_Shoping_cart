import json
from pprint import pprint
import boto3
import requests


def lambda_handler(event, context):
    LIST_GUEST_CART_ENDPOINT = "https://wxbh5t09za.execute-api.us-east-1.amazonaws.com/default/list_cart_guest"

    dynamodb = boto3.resource('dynamodb')
    user_table = dynamodb.Table('users')
    user_cart_table = dynamodb.Table('user_cart')
    anonymous_cart_table = dynamodb.Table('guest_cart')
    user_table = dynamodb.Table('users')
    data = event['body']
    # data = json.loads(data)
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']

        # Retrieve the user item from the DynamoDB table
        response = user_table.get_item(Key={'username': username})
        user_item = response.get('Item')

        if user_item and user_item.get('password') == password:

            if (data['cart_id']):
                cart_items = anonymous_cart_table.get_item(
                    Key={'cart_id': data['cart_id']})['Item']
                pprint(cart_items)
                user_cart_table.put_item(
                    Item={"cart_id": data['cart_id'], "item_id": cart_items['item_id'], "username": data['username']})

            return {
                'statusCode': 200,
                'body': json.dumps({"msg": "Login Sucess", "user_id": user_item.get('user_id'), "name": user_item.get('name')})
            }
        else:
            return {
                'statusCode': 401,
                'body': 'Invalid username or password'
            }
    else:
        return {
            'statusCode': 400,
            'body': 'Username and password are required'
        }


res = lambda_handler({"body": {"username": "dikshant", "password": "pass",
                     "cart_id": "37a58683-5ac2-4a40-9334-77a6e12ea50a"}}, "awdwd")

print(res)
