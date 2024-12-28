from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image

# Image validation function
def validate_image_format(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError):
        raise ValidationError("Uploaded file is not a valid image.")

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/categories/', validators=[validate_image_format])

    def __str__(self):
        return self.name

# Product model
class Store(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/products/', validators=[validate_image_format])
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rate = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Brand model
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Order model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

        

# Payment model
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Paystack', 'Paystack'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=50, default='Pending')  # Updated default
    reference = models.CharField(max_length=100, unique=True)  # For Paystack reference
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()

# Review model
class Review(models.Model):
    product = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Wishlist model
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='wishlist_items')

    class Meta:
        unique_together = ('user', 'product')
