import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    user_table = dynamodb.Table('users')
    # anonymous_cart_table = dynamodb.user_table('userData')

    data = event['body']
    data = json.loads(data)
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']

        # Retrieve the user item from the DynamoDB table
        response = user_table.get_item(Key={'username': username})
        user_item = response.get('Item')

        if user_item and user_item.get('password') == password:
            return {
                'statusCode': 200,
                'body': 'Login successful'
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
