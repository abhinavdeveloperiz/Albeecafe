from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='product/')
   


    def __str__(self):
        return self.name
    
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    featured = models.BooleanField(default=False)  # Top slider image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
    
    