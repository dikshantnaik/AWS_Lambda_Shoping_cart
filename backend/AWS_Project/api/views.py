import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import requests

REGISTER_ENDPOINT = "https://riwt5hd79f.execute-api.us-east-1.amazonaws.com/default/register_user"


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
            return HttpResponseRedirect("/products")
