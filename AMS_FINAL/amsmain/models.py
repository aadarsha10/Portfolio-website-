from django.db import models


# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    date = models.DateField()
    event = models.CharField(max_length=200)
    description = models.TextField()


class InsertImage(models.Model):
    imagename = models.CharField(max_length=255)
    image = models.FileField()
    category = models.CharField(max_length=255)
