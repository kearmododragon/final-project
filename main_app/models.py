from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(null=True, blank=True, max_length=5000)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField("Country name:", unique=True, max_length=300)
    image = models.URLField("URL image representing the country", null=True, blank=True, max_length=5000)
    mapsURL = models.URLField("Maps url", null=True, blank=True, max_length=5000)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.name

class City(models.Model):
    name = models.CharField("City", max_length=300,)
    image = models.URLField("Map", null=True, blank=True, max_length=5000)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    mapsURL = models.URLField("Maps link", null=True, blank=True, max_length=5000)

    def __str__(self):
        return self.name
    
class Holiday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,  default="holiday")
    arrivalDate = models.DateField("Left home", auto_now=True)
    deparureDate = models.DateField("Returned", auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    companions = models.CharField(max_length=1000,  default="friend") 
        
    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="event", max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name