from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural= "categories"

class Item(models.Model):
    listing_category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) 
    listing_name = models.CharField(max_length=255)
    listing_description = models.TextField(blank=True, null= True)
    listing_price = models.FloatField(blank=True, null=True)
    listing_image = models.ImageField(upload_to="item_images", blank=True, null= True)
    listing_is_sold = models.BooleanField(default=False)
    listing_created_at = models.DateTimeField(auto_now_add=True)
    listing_created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    def __str__(self):
        return self.listing_name