import email
from pyexpat import model
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    