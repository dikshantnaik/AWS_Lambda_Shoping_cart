data = [
    {
        "product_name": {
            "S": "Banana"
        },
        "product_category": {
        },
        "product_id": {
            "S": "hahahawd"
        },
        "product_price": {
            "N": "500"
        }
    },
    {
        "product_name": {
            "S": "Banana"
        },
        "product_category": {
            "S": "fruit"
        },
        "product_id": {
            "S": "awdd"
        },
        "product_price": {
            "N": "500"
        }
    },
    {
        "product_name": {
            "S": "Banana"
        },
        "product_category": {
            "S": "fruit"
        },
        "product_id": {
            "S": "ijbjbjbij"
        },
        "product_price": {
            "N": "500"
        }},
    {
        "product_name": {
            "S": "Banana"
        },
        "product_category": {
            "S": "fruit"
        },
        "product_id": {
            "S": "fuckyou"
        },
        "product_price": {
            "N": "500"
        }
    },
    {
        "product_name": {
            "S": "Banana"
        },
        "product_category": {
            "S": "fruit"
        },
        "product_id": {
            "S": "hahah"
        },
        "product_price": {
            "N": "500"
        }
    }
]
products = []
for item in data:
    product = {
        'product_name': item['product_name']['S'],
        'product_category': item['product_category']['S'],
        'product_id': item['product_id']['S'],
        'product_price': int(item['product_price']['N'])
    }
    products.append(product)

print(products)
# for product in products:
# print(product)
