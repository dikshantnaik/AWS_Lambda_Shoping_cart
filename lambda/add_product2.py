import json
import boto3
from uuid import uuid4

response = {}


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    cart_table = dynamodb.Table('products')
    # anonymous_cart_table = dynamodb.cart_table('userData')
    data = event['body']

    data = json.loads(data)
    # product_id =
    data["product_id"] = str(uuid4())
    # data = json.loads(data)
    cart_table.put_item(Item=data)
    response["response"] = "Product Added  Successfully"
    return {
        'statusCode': 200,
        "body": json.dumps(response)
    }
