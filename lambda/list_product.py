import boto3
import json


def lambda_handler(event, context):
    # Specify your DynamoDB table name
    table_name = 'products'

    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')

    try:
        # projection_expression = 'product_name, product_category, product_id, product_price,'

        # Retrieve all items from the DynamoDB table with the specified projection expression
        response = dynamodb.scan(
            TableName=table_name
        )

        # Extract the items from the response
        items = response['Items']
        print(items)
        simplified_array = []
        # Iterate over the items and print the data
        for item in items:
            simplified_item = {}
            for key, value in item.items():
                simplified_item[key] = list(value.values())[0]
            simplified_array.append(simplified_item)

        return {
            'statusCode': 200,
            'body': json.dumps(simplified_array)
        }

    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': 'Error listing data from DynamoDB'
        }
