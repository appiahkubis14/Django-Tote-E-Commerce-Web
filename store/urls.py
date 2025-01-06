from django.urls import path
from .views import (
    shop,
    add_to_cart,
    index,
    about,
    shop_single,
    # register,
    Login,
    blog,
    contact,
    view_cart,
    remove_from_cart,
    update_cart,
    checkout_view,
    initialize_payment,
    process_payment,
    verify_payment,
    process_order,
    base,
    Signup
)

urlpatterns = [

    path('',index, name='index'),

    path('about/', about, name='about'),  # About page

    path('shop-single/', shop_single, name='shop_single'),  # Single product page

    path('register/', Signup.as_view(), name='register'),  # Register page

    path('login/', Login.as_view(), name='login'),  # Login page

    path('blog/', blog, name='blog'),  # Blog page
    
    path('contact/', contact, name='contact'),

    path('shop/', shop, name='shop'),

    path('base/', base, name='base'),

    path('cart/', view_cart, name='cart'),

    path('checkout/', checkout_view, name='checkout'),

    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),

    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

    path('update/<int:item_id>/', update_cart, name='update_cart'),

    path('process_payment/', process_payment, name='process_payment'),

    path('payment/initialize/<int:order_id>/', initialize_payment, name='initialize_payment'),

    path('payment/verify/', verify_payment, name='verify_payment'),

    path('process_order/', process_order, name='process_order'),
]


