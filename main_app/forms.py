from django.forms import ModelForm
from .models import Country, City, Holiday

class CountryForm(ModelForm):
  class Meta:
    model = Country
    fields = ['name', 'image', "mapsURL", "continent",]

class CityForm(ModelForm):
  class Meta:
    model = City
    fields = ["name", "image", "mapsURL", "country", "continent",]

class HolidayForm(ModelForm):
  class Meta:
    model = Holiday
    fields =["name", "city", "companions",]