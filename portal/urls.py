from django.urls import path
from .views import (
    index,
    about,
    shop_now,
    shop_single,
    cart,
    checkout,
    register,
    login,
    blog,
    contact,
)

urlpatterns = [
    path('', index, name='index'),  # Home page

    path('about/', about, name='about'),  # About page

    path('shop/', shop_now, name='shop'),  # Shop page

    path('shop-single/', shop_single, name='shop_single'),  # Single product page

    path('cart/', cart, name='cart'),  # Cart page

    path('checkout/', checkout, name='checkout'),  # Checkout page

    path('register/', register, name='register'),  # Register page

    path('login/', login, name='login'),  # Login page

    path('blog/', blog, name='blog'),  # Blog page
    
    path('contact/', contact, name='contact'),  # Contact page
]
