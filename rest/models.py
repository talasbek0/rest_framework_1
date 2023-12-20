from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.TextField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class Person(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)