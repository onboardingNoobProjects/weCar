from django.shortcuts import render
from .models import Deal
from django.http import Http404


# Create your views here.

def index(request):
    all_deals = Deal.objects.all()
    return render(request, 'weCar/index.html', {'all_deals' : all_deals})

def detail(request, deal_id):
    try:
        deal = Deal.objects.get(pk=deal_id)
    except Deal.DoesNotExist:
        raise Http404("Deal cannot be found")
    return render(request, 'weCar/detail.html', {'deal': deal})
