from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(max_length=300)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title