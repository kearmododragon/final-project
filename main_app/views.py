from django.shortcuts import render, redirect
from .models import Continent, Country 
from .forms import CountryForm
from .forms import CityForm 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


countries = [
   
]

cities =[
   
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def holidays(request):
    return render(request, 'holidays.html')

def locations_landing(request):
   return render (request, "locations/landing.html")

def continents_index(request):
    continents = Continent.objects.all()
    return render(request, 'continents/index.html',{
     "continents": continents  
    } 
)

def continents_detail(request, continent_id):
    continent = Continent.objects.get(id=continent_id)
    country_form = CountryForm()
    return render(request, 'continents/detail.html', {
        "continent": continent,
        "country_form": country_form 
    })

def add_country(request, continent_id):
    form = CountryForm(request.POST)
    if form.is_valid():
      new_country = form.save(commit=False)
      new_country.continent_id = continent_id
      new_country.save()
    return redirect("detail", continent_id = continent_id)

def countries_index(request):
    return render(request, 'countries/index.html',{
     "countries": countries  
    } 
)

def countries_detail(request, continent_id, country_id):
    country = Country.objects.get(id=country_id)
    city_form = CityForm()
    return render(request, 'countries/detail.html', {
        "country": country,
        "city_form": city_form 
    })

def add_city(request, country_id, continent_id):
    form = CityForm(request.POST)
    if form.is_valid():
      new_city = form.save(commit=False)
      new_city.country_id = country_id
      new_city.save()
    return redirect("detail", country_id = country_id)


def cities_index(request):
    return render(request, 'cities/index.html',{
     "cities": cities  
    } 
)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
