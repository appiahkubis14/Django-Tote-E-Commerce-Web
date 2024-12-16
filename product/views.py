# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Product, Cart, Order
# from .serializers import ProductSerializer, CartSerializer, OrderSerializer
# from django.http import JsonResponse
# from .models import ProductCategory


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_product(request):
#     """Create a new product."""
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_to_cart(request):
#     """Add a product to the cart."""
#     product = get_object_or_404(Product, id=request.data['product_id'])
#     quantity = request.data.get('quantity', 1)
#     cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
#     cart_item.quantity += int(quantity)
#     cart_item.save()
#     return Response({'message': 'Item added to cart'})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_order(request):
#     """Create an order from the cart."""
#     cart_items = Cart.objects.filter(user=request.user)
#     if not cart_items:
#         return Response({'error': 'Cart is empty'}, status=400)
    
#     total_amount = sum(item.product.price * item.quantity for item in cart_items)
#     order = Order.objects.create(user=request.user, total_amount=total_amount)
#     order.products.set(cart_items)
#     order.save()
#     cart_items.delete()  # Clear the cart after creating the order
#     return Response({'message': 'Order created successfully'})


# #============================================================================
# @api_view(['GET'])
# def retrieve_product(request, pk):
#     """Retrieve a single product."""
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)

# @api_view(['GET'])
# def list_products(request,slug=None):
#     category = None
#     product = None 

#     if slug != None:
#         category = get_object_or_404(slug=slug)
#         products = Product.objects.all().filter(category = category , is_available=True)
#         product_count = product.count()

#     else:
#         """Fetch all products."""
#         products = Product.objects.all().filter(is_available=True)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def fetch_user_cart(request):
#     """Fetch cart items for the authenticated user."""
#     carts = Cart.objects.filter(user=request.user)
#     serializer = CartSerializer(carts, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def fetch_user_orders(request):
#     """Fetch orders for the authenticated user."""
#     orders = Order.objects.filter(user=request.user)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_categories(request):
#     categories = ProductCategory.objects.all().values('name', 'image')  # Assuming 'name' and 'icon' fields
#     categories_list = list(categories)  # Convert QuerySet to a list of dictionaries
#     return JsonResponse(categories_list, safe=False)

# #============================================================================


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_product(request, pk):
#     """Update a product."""
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_cart_item(request, pk):
#     """Update the quantity of a cart item."""
#     cart_item = get_object_or_404(Cart, id=pk, user=request.user)
#     cart_item.quantity = request.data.get('quantity', cart_item.quantity)
#     cart_item.save()
#     return Response({'message': 'Cart item updated successfully'})



# #============================================================================


# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_cart_item(request, pk):
#     """Remove an item from the cart."""
#     cart_item = get_object_or_404(Cart, id=pk, user=request.user)
#     cart_item.delete()
#     return Response({'message': 'Item removed from cart'}, status=204)


# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_product(request, pk):
#     """Delete a product."""
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     return Response({'message': 'Product deleted successfully'}, status=204)


# # ORDER OPERATIONS



# #============================================================================

# def homepage(request):
#     categories = ProductCategory.objects.all()
#     return render(request, 'portal/index.html', {'categories': categories})




