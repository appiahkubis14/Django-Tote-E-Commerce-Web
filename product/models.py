from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image


def validate_image_format(image):
    try:
        img = Image.open(image)
        img.verify()  # Verify that it is an image
    except (IOError, SyntaxError):
        raise ValidationError("Uploaded file is not a valid image.")

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', validators=[validate_image_format])
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_carts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart"

    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_orders')
    products = models.ManyToManyField(Cart)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"




class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/',blank=True, null=True)

    def __str__(self):
        return self.name

























