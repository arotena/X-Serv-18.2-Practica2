from django.db import models

# Create your models here.
class Page(models.Model):
    url_original = models.TextField()
