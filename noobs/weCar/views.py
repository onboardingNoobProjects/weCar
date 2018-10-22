from django.shortcuts import render
from django.http import HttpResponse
# from .models import deals
import json


# Create your views here.
data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

sampleData = json.dumps(data)




def index(request):
    return HttpResponse('This is the homepage')

def wecar(request):
    html = ''
    return HttpResponse(html)

def api(request):
    return HttpResponse(sampleData)
