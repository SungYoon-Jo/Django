from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=True)
    
# class List(models.Model):
#     title = models.CharField(max_length=20, null=True)
#     content = models.TextField()
#     writer = models.CharField(max_length=20, null=True)