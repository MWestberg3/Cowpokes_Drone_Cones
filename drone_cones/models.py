from django.db import models

# Create your models here.

class Account(models.Model):
    Id = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    cart = models.JSONField(null=True)

class Drone(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    droneName = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    scoops = models.IntegerField()
    isActive = models.BooleanField(default = False)
    dateRegistered = models.DateField()

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    items = models.JSONField()
    drone = models.IntegerField()
    deliverySuccessful = models.BooleanField()
    timeOrdered = models.DateField()
    timeDelivered = models.DateField()
    timeToDeliver = models.DateField()

class Admins(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    accessLevel = models.CharField(max_length=100)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    stockAvailable = models.IntegerField()
