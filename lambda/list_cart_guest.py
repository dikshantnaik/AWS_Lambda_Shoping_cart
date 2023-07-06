import json
import boto3


def lambda_handler(event, context):
    # TODO implement

    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Define the table name
    product_table_name = 'products'
    guest_cart_table_name = "guest_cart"

    guest_cart_table = dynamodb.Table(guest_cart_table_name)
    product_table = dynamodb.Table(product_table_name)

    cart_id = event['queryStringParameters']['cart_id']

    response = guest_cart_table.get_item(Key={'cart_id': cart_id})
    Items = response['Item']

    cart_items = []
    for item in Items['item_id']:
        product = product_table.get_item(Key={'product_id': item})
        # print(product['Item'])
        product['Item']['product_price'] = str(
            product['Item']['product_price'])
        cart_items.append(product['Item'])

    print(cart_items)
    return {
        'statusCode': 200,
        'body': json.dumps(cart_items)
    }
