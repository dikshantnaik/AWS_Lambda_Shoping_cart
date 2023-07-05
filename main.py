from uuid import uuid4

data = {
    'product_name': 'Banana',
    'product_price': 500,
    'product_discription': 'A Cool Procuct '
}
data['product_id'] = str(uuid4())


print(data)
