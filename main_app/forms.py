from django.forms import ModelForm
from .models import Country

class CountryForm(ModelForm):
  class Meta:
    model = Country
    fields = ['name', 'image', "mapsURL", "continent",]
