from django.db import models

# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(null=True, blank=True, max_length=5000)


class Country(models.Model):
    name = models.CharField(max_length=300)
    continent = models.ForeignKey
    image = models.URLField
    mapsURL = models.URLField
    
    def __str__(self):
       return self.name

class City(models.Model):
    name = models.CharField(max_length=300)
    image = models.URLField
    country = models.ForeignKey

    def __str__(self):
        return self.name

