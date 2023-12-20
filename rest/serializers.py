from .models import *
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['username', 'email', 'password']
