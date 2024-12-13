from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # Product URLs
    path('products/', views.list_products, name='list_products'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:pk>/', views.retrieve_product, name='retrieve_product'),
    path('products/<int:pk>/update/', views.update_product, name='update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),

    # Cart URLs
    path('cart/', views.fetch_user_cart, name='fetch_user_cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:pk>/update/', views.update_cart_item, name='update_cart_item'),
    path('cart/<int:pk>/delete/', views.delete_cart_item, name='delete_cart_item'),

    # Order URLs
    path('orders/', views.fetch_user_orders, name='fetch_user_orders'),
    path('orders/create/', views.create_order, name='create_order'),

    path('categories/',views.get_categories, name='get_categories'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)