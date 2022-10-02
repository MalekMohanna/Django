from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def validator(self,data):
        errors={}
        if len(data['show-t']) < 2 :
            errors['title']='Title should be at least 2 characters'
        if len(data['netw']) < 3 :
            errors['network']='Network should be at least 3 characters'
        if len(data['descr']) < 10 :
            errors['descreption']='Descreption should be at least 10 characters'
        return errors

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    descreption=models.TextField(default='To be added')
    release_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)
    objects= ShowManager()

