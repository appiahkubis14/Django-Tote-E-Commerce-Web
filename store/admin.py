from django.utils.html import format_html
from django.contrib import admin
# from .models import Product, Cart, Order
# from django.contrib import admin
from .models import StoreModel


@admin.register(StoreModel)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price', 'rate', 'image_preview','description')  # Fields to display in the list view
    search_fields = ('name',)                                 # Enable search by name
    list_filter = ('rate',)                                   # Add filter by rate
    ordering = ('name',)      
    
    prepopulated_fields = {'slug':('name',)}
 

    def image_preview(self, obj):
        """Display an image preview in the admin list view."""
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"
