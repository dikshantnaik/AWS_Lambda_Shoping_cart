import requests
from django.shortcuts import render

LIST_PRODUCT_ENDPOINT = "https://6owwy9eo22.execute-api.us-east-1.amazonaws.com/default/listt_product"
LIST_GUEST_CART_ENDPOINT = "https://wxbh5t09za.execute-api.us-east-1.amazonaws.com/default/list_cart_guest"


def products_view(request):

    response = requests.get(LIST_PRODUCT_ENDPOINT)
    products = response.json()
    return render(request, 'products.html', {'products': products})


def cart_view(request):
    cart_id = request.session.get('cart_id')
    response = requests.get(LIST_GUEST_CART_ENDPOINT+"?cart_id="+cart_id)
    cart_items = response.json()
    print(cart_items)
    return render(request, 'cart.html', {'cart': cart_items})


def register_view(request):

    return render(request, "register.html")


def add_to_cart_view(request):
    url = "https://gmzungq13g.execute-api.us-east-1.amazonaws.com/default/add_to_cart_guest"
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if request.session.get('cart_id'):
            cart_id = request.session.get('cart_id')
            url = f"{url}?cart_id={cart_id}&item_id={item_id}"
        else:
            url = f"{url}?item_id={item_id}"
        res = requests.get(url)
        print(url)
        context = {
            'show_alert': True,
            'alert_message': 'Added to CART !',
        }
        data = res.json()
        if not request.session.get('cart_id'):
            request.session['cart_id'] = data['cart_id']

        return render(request, 'products.html', context)
