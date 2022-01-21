from email.headerregistry import Address
from django.db import models

class employee(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField()
    Phone = models.CharField(max_length=10)
# Create your models here.
