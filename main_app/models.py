from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(null=True, blank=True, max_length=5000)
    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField("Country", max_length=300)
    image = models.URLField("Map", null=True, blank=True, max_length=5000)
    mapsURL = models.URLField("Maps link", null=True, blank=True, max_length=5000)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.name

class City(models.Model):
    name = models.CharField(max_length=300)
    image = models.URLField(null=True, blank=True, max_length=5000)
    country = models.ForeignKey
    mapsURL = models.URLField(null=True, blank=True, max_length=5000)

    def __str__(self):
        return self.name
    

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    arrivalDate = models.DateField
    deparureDate = models.DateField
    companions = models.CharField
    

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
