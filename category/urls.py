from django.urls import path
from .views import list_category

urlpatterns = [
    path('<slug:slug>/', list_category, name='product_category'),
]
