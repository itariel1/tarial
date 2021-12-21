from django.db import models

# Create your models here.
# class Anime(models.Model):
#     title = models.CharField(max_length=255)
#     image = models.ImageField()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()