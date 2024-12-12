from django.shortcuts import render



def index(request):
    return render(request, 'portal/index.html', locals())


def about(request):
    return render(request, 'portal/about.html', locals())


def shop_now(request):
    return render(request, 'portal/shop.html', locals())


def shop_single(request):
    return render(request, 'portal/shop-single.html', locals())


def cart(request):
    return render(request, 'portal/cart.html', locals())


def checkout(request):
    return render(request, 'portal/checkout.html', locals())


def register(request):
    
    return render(request, 'portal/register.html', locals())


def login(request):
    return render(request, 'portal/login.html', locals())


def blog(request):
    return render(request, 'portal/blog.html', locals())


def contact(request):
    return render(request, 'portal/contact.html', locals())

