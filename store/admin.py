from django.contrib import admin
from .models import  Category, Store, Brand, Order, OrderItem, Payment, Cart, Review, Wishlist


# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','image')
    search_fields = ('name',)
    ordering = ('name',)

# Register the Store model
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price', 'stock', 'is_available', 'category', 'image','created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('is_available', 'category')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)

# Register the Brand model
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the Order model
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    # Ensure these fields are valid
    list_display = ('customer', 'total_price', 'created_at', 'reference')  # Remove 'user', 'status', 'updated_at'
    list_filter = ('created_at', 'total_price')  # Update to valid fields like 'created_at'

    # You can also define custom methods in the admin for non-field attributes
    def user(self, obj):
        return obj.customer.name  # Assuming 'customer' is related to a user

    def status(self, obj):
        return obj.payment.payment_status  # You might want to pull status from Payment model

    def updated_at(self, obj):
        return obj.modified_at  # Assuming you add a 'modified_at' field in your Order model

admin.site.register(Order, OrderAdmin)

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
