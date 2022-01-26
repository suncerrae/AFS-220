from django.db import models

# Create your models here.

class Menu_Item(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    price = models.CharField(max_length=300)    
    img = models.CharField(max_length=300)
    url = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name

class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Carts(models.Model):
    name = models.CharField(max_length = 100)
    meat = models.CharField(max_length = 100)
    side1 = models.CharField(max_length = 100)
    side2 = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Side(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name