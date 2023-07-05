import json
import boto3
from uuid import uuid4

response = {}


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    cart_table = dynamodb.Table('guest_cart')
    # anonymous_cart_table = dynamodb.cart_table('userData')
    data = event['body']
    if "cart_id" not in data:
        cart_id = str(uuid4())
        data['cart_id'] = cart_id
        cookie = f"cart_id={cart_id}; Path=/; Max-Age=604800; Secure; HttpOnly"

    cart_table.put_item(Item=data)
    response["response"] = "Added to Cart Successfully"

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Set-Cookie': cookie
        },
        "body": response
    }
