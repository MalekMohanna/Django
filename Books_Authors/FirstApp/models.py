from email.policy import default
from turtle import title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="To be added")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    books = models.ManyToManyField(Book,related_name="authors")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

