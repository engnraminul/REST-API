from dataclasses import fields
from rest_framework import serializers
from .models import Blog, Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
        #fields=['name', 'email', 'phone', 'subject', 'details']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        #fields = '__all__'
        exclude = ['is_active', 'user',]



class BlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        