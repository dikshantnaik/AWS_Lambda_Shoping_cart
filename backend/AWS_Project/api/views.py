from constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT
import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import requests
import sys
sys.path.append("..")


def register_view(request):
    if request.method == 'POST':
        if (request.POST.get('password') == request.POST.get('confirmPassword')):
            data = {
                "username": request.POST.get('username'),
                "name": request.POST.get('name'),
                "password": request.POST.get('password'),
            }
            print(data)
            response = requests.post(REGISTER_ENDPOINT, json=data)

            print(response.text)
            return HttpResponse('Registered ')


def login_view(request):
    if request.method == "POST":

        data = {
            "username": request.POST.get('username'),
            "password": request.POST.get('password'),
        }
        if request.session.get('cart_id'):
            data['cart_id'] = request.session.get('cart_id')
        response = requests.post(LOGIN_ENDPOINT, json=data)

        data = response.json()
        print(response.text)
        request.session['name'] = data['name']
        request.session['user_id'] = data['user_id']
        return HttpResponse(data['msg'])
