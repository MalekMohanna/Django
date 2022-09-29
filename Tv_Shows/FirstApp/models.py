from email.policy import default
from django.db import models

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    descreption=models.TextField(default='To be added')
    release_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)
