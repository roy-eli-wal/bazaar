from django.db import models

from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Chat(models.Model):
    listing = models.ForeignKey(Item, related_name='chat', on_delete=models.CASCADE)
    community = models.ManyToManyField(User, related_name='chat')
    created_listing_at = models.DateTimeField(auto_now_add=True)
    modified_listing_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_listing_at',)
    
class Messages(models.Model):
    message = models.ForeignKey(Chat, related_name='all_msgs', on_delete=models.CASCADE)
    broadcasting = models.TextField()
    date_at = models.DateTimeField(auto_now_add=True)
    generated_by = models.ForeignKey(User, related_name='generated_msgs', on_delete=models.CASCADE)