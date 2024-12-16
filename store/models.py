from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image
from django.conf import settings
from category.models import Category


def validate_image_format(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError):
        raise ValidationError("Uploaded file is not a valid image.")

class StoreModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/products/', validators=[validate_image_format])
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255,blank=True, null=True)
    rate = models.IntegerField()
    slug = models.SlugField(max_length=255)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.name