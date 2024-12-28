from django.shortcuts import render
from .models import Category


# Create your views here.
# @receiver(pre_save, sender=Category)
# def auto_populate_slug(sender, instance, **kwargs):
#     if not instance.slug:  # Only set the slug if it's not already populated
#         instance.slug = slugify(instance.category_name)


# @api_view(['GET'])
def list_category(request,slug=None):
    category = None
    product = None 

    if slug != None:
        category = get_object_or_404(slug=slug)
        products = Product.objects.filter(category = category , is_active=True)
        product_count = product.count()

    else: 
        """Fetch all products."""
        products = Product.objects.filter(is_active=True)
        # serializer = ProductSerializer(products, many=True)
        return
