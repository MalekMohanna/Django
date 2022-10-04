from email.policy import default
from django.db import models
from FirstApp.models import User
# Create your models here.

class BookManager(models.Manager):
    def book_validation(self,data):
        errors={}
        if len(data['title'])<2:
            errors["title"] = "You must enter a title"
        if len(data['description'])<5:
            errors["description"] = "Description should be at least 5 charachters"
        return errors

    def update_validator(self, data):
        errors = {}
        if len(data['title'])<2:
            errors["title"] = "You must enter a title"
        if len(data['description']) < 5:
            errors ['update_description'] = "Description should be at least 5 characters"
        return errors

class Book(models. Model) :
    title = models.CharField (max_length=255)
    description = models.TextField(null=True)
    uploadedby = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    userswho_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= BookManager()