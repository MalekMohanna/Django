# Generated by Django 2.2.4 on 2022-09-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
