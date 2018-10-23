from django.shortcuts import render
from django.http import HttpResponse
from .models import Deal
from django.template import loader
from django.shortcuts import render
import json


# Create your views here.

def index(request):
    all_deals = Deal.objects.all()
    context = {'all_deals' : all_deals}
    return render(request, 'weCar/index.html', context)

def detail(request, deal_id):
    html = "<h2>Details for deals id: " + str(deal_id) + "</h2>"
    return HttpResponse(html)
