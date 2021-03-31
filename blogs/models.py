from django.db import models
from PIL import Image

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now=True)


