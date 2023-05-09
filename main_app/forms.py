from django.forms import ModelForm
from .models import Country, City

class CountryForm(ModelForm):
  class Meta:
    model = Country
    fields = ['name', 'image', "mapsURL", "continent",]

class CityForm(ModelForm):
  class Meta:
    model = City
    fields = ["name", "image", "mapsURL", "country", "continent",]