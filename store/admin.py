from django.contrib import admin
from .models import Category, Store, Order, OrderItem, Payment, Cart, Review, Wishlist, Customer
from PIL import Image
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

# Image validation function
def validate_image_format(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError):
        raise ValidationError("Uploaded file is not a valid image.")


# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)
    ordering = ('name',)


# Register the Store model
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price', 'stock', 'is_available', 'category', 'image', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('is_available', 'category')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)


# Register the Order model
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'created_at', 'reference')
    list_filter = ('created_at', 'total_price')


# Register the Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'amount', 'payment_method', 'payment_status', 'created_at')
    list_filter = ('payment_method', 'payment_status')
    search_fields = ('order__id', 'user__username', 'payment_method')


# Register the Cart model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    search_fields = ('user__username', 'product__name')


# Register the Review model
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('product__name', 'user__username')


# Register the Wishlist model
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__username', 'product__name')


# Register the Customer mode

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('is_active', 'is_staff', 'is_admin')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
        # ('Important Dates', {'fields': ('date_joined',)}),  # Exclude 'last_login'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Register the admin
admin.site.register(Customer, CustomerAdmin)
