from dataclasses import fields
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
        #fields=['name', 'email', 'phone', 'subject', 'details']