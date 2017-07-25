from django.db import models
from datetime import datetime

class UrlTable(models.Model):
    short_url = models.CharField(max_length=100)
    long_url = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=datetime.now())
# Create your models here.
