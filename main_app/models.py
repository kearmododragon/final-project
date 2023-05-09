from django.db import models

# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField

class Country(models.Model):
    name = models.CharField(max_length=300)
    continent = models.ForeignKey
    mapsURL = models.URLField

class City(models.Model):
    name = models.CharField(max_length=300)
    country = models.ForeignKey

