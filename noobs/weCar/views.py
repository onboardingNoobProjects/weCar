from django.shortcuts import render
from django.http import HttpResponse
from .models import Deal
from django.template import loader

import json


# Create your views here.





def index(request):
    all_deals = Deal.objects.all()
    template = loader.get_template('weCar/index.html')
    context = {
         'all_deals' : all_deals,
    }

    # html = ''
    # for deal in all_deals:
    #     url = '/wecar/' + str(deal.id) + '/'
    #     html += '<a href="' + url +  '">' + deal.title + '</a><br>'
    return HttpResponse(template.render(context, request))

def detail(request, deal_id):
    html = "<h2>Details for deals id: " + str(deal_id) + "</h2>"
    return HttpResponse(html)
