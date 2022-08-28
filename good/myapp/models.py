from email.mime import image
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()
    writer = models.CharField(max_length=30, null=False)
    photo = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title
    