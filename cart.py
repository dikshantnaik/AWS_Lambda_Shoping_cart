import json
import boto3
from uuid import uuid4

response = {}


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    cart_table = dynamodb.Table('guest_cart')
    # anonymous_cart_table = dynamodb.cart_table('userData')
    data = event['body']

    cart_table.put_item(Item=data)
    response["response"] = "Registerd Success"

    return {
        'statusCode': 200,
        "body": response
    }
