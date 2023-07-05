import json
import boto3

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Define the table name
product_table_name = 'products'
guest_cart_table_name = "guest_cart"

guest_cart_table = dynamodb.Table(guest_cart_table_name)
product_table = dynamodb.Table(product_table_name)


cart_id = "37a58683-5ac2-4a40-9334-77a6e12ea50a"


response = guest_cart_table.get_item(Key={'cart_id': cart_id})
Items = response['Item']

cart_items = []
for item in Items['item_id']:
    product = product_table.get_item(Key={'product_id': item})
    # print(product['Item'])
    product['Item']['product_price'] = str(product['Item']['product_price'])
    cart_items.append(product['Item'])
print(cart_items)
print(cart_items[0]['product_id'])
jsss = json.dumps(cart_items)
# # Define the keys for the items you want to retrieve
# keys = [
#     {'product_id': {'S': '3e310daa-d58a-45db-8a34-f5f1c75d36e8'}},
#     {'product_id': {'S': '2cf7bdf6-963d-4b9f-bc15-0355e56222aa'}},
#     # Add more keys as needed
# ]

# # Create a request to retrieve the items
# request_items = {
#     product_table_name: {
#         'Keys': keys
#     }
# }

# # Retrieve the items using batch_get_item
# response = dynamodb.batch_get_item(RequestItems=request_items)

# # Check if the response contains the requested items
# if 'Responses' in response and product_table_name in response['Responses']:
#     items = response['Responses'][product_table_name]
#     for item in items:
#         # Process each item as needed
#         print(item)
# else:
#     print('No items found.')
