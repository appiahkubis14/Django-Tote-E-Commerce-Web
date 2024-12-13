from django.utils.html import format_html
from django.contrib import admin
from .models import Product, Cart, Order
from django.contrib import admin
from .models import ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price', 'rate', 'image_preview')  # Fields to display in the list view
    search_fields = ('name',)                                 # Enable search by name
    list_filter = ('rate',)                                   # Add filter by rate
    ordering = ('name',)                                      # Default ordering by name

    def image_preview(self, obj):
        """Display an image preview in the admin list view."""
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_on', 'total_price_display')
    search_fields = ('user__username', 'product__name')  # Enable search by user and product name
    list_filter = ('added_on',)                         # Add filter by addition date
    ordering = ('-added_on',)                           # Default ordering by latest added

    def total_price_display(self, obj):
        """Display the total price of the cart item."""
        return obj.total_price()
    total_price_display.short_description = "Total Price"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'created_at', 'product_list')  # Fields to display in the list view
    search_fields = ('user__username',)                                   # Enable search by username
    list_filter = ('created_at',)                                         # Add filter by creation date
    ordering = ('-created_at',)                                           # Default ordering by latest created
    filter_horizontal = ('products',)                                     # Allow easy selection of multiple products

    def product_list(self, obj):
        """Display the list of products in the order."""
        return ", ".join([f"{item.product.name} (x{item.quantity})" for item in obj.products.all()])
    product_list.short_description = "Products"



class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')  # Display name and icon in the admin list view
    search_fields = ('name',)  # Allow searching by name
    list_filter = ('name',)  # Optional: Add filters based on name

# Register the model with the admin interface
admin.site.register(ProductCategory, ProductCategoryAdmin)
