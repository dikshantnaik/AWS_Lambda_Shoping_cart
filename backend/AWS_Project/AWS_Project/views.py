import requests
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from constants import *


def index_view(request):
    return HttpResponseRedirect("/products/")


def products_view(request):

    response = requests.get(LIST_PRODUCT_ENDPOINT)
    products = response.json()
    if request.session.get('name'):

        return render(request, 'products.html', {'products': products, 'name': request.session.get('name')})
    else:
        return render(request, 'products.html', {'products': products})


def cart_view(request):
    cart_id = request.session.get('cart_id')
    response = requests.get(LIST_GUEST_CART_ENDPOINT+"?cart_id="+cart_id)
    cart_items = response.json()
    print(cart_items)
    return render(request, 'cart.html', {'cart': cart_items})


def register_view(request):

    return render(request, "register.html")


def login_view(request):

    return render(request, 'login.html')


def add_to_cart_view(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if request.session.get('cart_id'):
            cart_id = request.session.get('cart_id')
            url = f"{ADD_TO_GUEST_CART_ENDPOINT}?cart_id={cart_id}&item_id={item_id}"
        else:
            url = f"{ADD_TO_GUEST_CART_ENDPOINT}?item_id={item_id}"
        res = requests.get(url)
        print(url)
        context = {
            'show_alert': True,
            'alert_message': 'Added to CART !',
            'url': "/products"
        }
        data = res.json()
        if not request.session.get('cart_id'):
            request.session['cart_id'] = data['cart_id']

        return render(request, 'products.html', context)
