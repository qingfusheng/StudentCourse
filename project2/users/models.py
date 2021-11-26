from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=255, null=True)
    name=models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
