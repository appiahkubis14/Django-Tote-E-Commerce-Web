from django.shortcuts import render
from store.models import Store

def index(request):
    products = Store.objects.all().filter(is_available=True)
    
    return render(request, 'portal/index.html', locals())


def shop(request):
    products = Store.objects.all().filter(is_available=True)
    
    return render(request, 'portal/shop.html',locals())