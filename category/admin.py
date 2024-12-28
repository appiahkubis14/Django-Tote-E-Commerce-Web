from django.contrib import admin
from django.utils.html import format_html
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'description', 'image_preview','is_active')

    def image_preview(self, obj):
        """Display an image preview in the admin list view."""
        if obj.image:  # Assuming the `Category` model has an `image` field
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"

# Register your models here.
admin.site.register(Category, CategoryAdmin)
