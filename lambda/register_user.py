import json
import boto3
from uuid import uuid4

response = {}


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    user_table = dynamodb.Table('users')
    # anonymous_cart_table = dynamodb.user_table('userData')
    data = event['body']
    data = json.loads(data)
    if data["username"]:
        response['response'] = "Username"
    else:
        response['response'] = "No Username"

    username = data['username']
    data["user_id"] = str(uuid4())
    if "Item" in user_table.get_item(Key={'username': username}):
        response["response"] = "Username Exists"
    else:
        user_table.put_item(Item=data)
        response["response"] = "Registerd Success"

    return {
        'statusCode': 200,
        "body": json.dumps(response)
    }
