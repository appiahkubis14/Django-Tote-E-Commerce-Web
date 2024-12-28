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

   
]
