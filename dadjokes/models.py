from django.db import models

# Create your models here.
class Joke(models.Model):
    text = models.TextField(blank=False)
    name = models.CharField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

class Picture(models.Model):
    image_url = models.URLField(blank=False)
    name = models.CharField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)