from django.shortcuts import render
from store.models import Store

def index(request):
    products = StoreModel.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'portal/index.html', context)


def shop(request):
    products = StoreModel.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'portal/shop.html',context)