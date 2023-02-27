from django.db import models

# Create your models here.
class Artwork(models.Model):
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    comments = models.CharField(max_length=100)
    image_url = models.CharField(max_length=1000)
    
    class Meta:
        ordering = ['category', 'subject']
    