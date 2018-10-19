from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json


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




def home(request):
    return HttpResponse('Hello, World!')

def api(request):
    return HttpResponse(sampleData)
