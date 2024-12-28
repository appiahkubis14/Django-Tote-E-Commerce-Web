from django.utils.text import slugify
from django.db import models

  
def validate_image_format(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError):
        raise ValidationError("Uploaded file is not a valid image.")

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/category/', blank=True, null=True,validators=[validate_image_format])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't exist
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
