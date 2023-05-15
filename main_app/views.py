from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Continent, Country, City, Holiday, Event 
from .forms import CountryForm, CityForm, HolidayForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from django.urls import reverse



def home(request):
    url = 'https://api.exchangerate.host/latest'
    currencies_to_display = ['USD', 'GBP', 'JPY']
    response = requests.get(url)
    data = response.json()
    rates = {currency: rate for currency, rate in data['rates'].items() if currency in currencies_to_display}
    return render(request, 'home.html', {'rates': rates})

def holidays_index(request):
    holidays = Holiday.objects.all()
    holiday_form = HolidayForm()
    return render(request, 'holidays/index.html',{
       "holidays" : holidays,
        "holiday_form": holiday_form,
    })

def holiday_detail(request, holiday_id):
    holidays=Holiday.objects.all()
    return render(request, 'countries/detail.html', {
        "holidays": holidays,
    })

def add_holiday(request):
    if request.method == 'POST':
        form = HolidayForm(request.POST)
        if form.is_valid():
            new_holiday = form.save()
            return redirect('holiday_detail', holiday_id=new_holiday.id)
    else:
        form = HolidayForm()
    return render(request, 'holiday_form.html', {
        'form': form
        })


def events_index(request):
   events = Event.objects.all()
   return render(request, 'events/index.html',{
      "events" : events
   })

def event_detail(request):
   return render(request)

def locations_landing(request):
    countries=Country.objects.all()
    return render (request, "locations/landing.html", {
        "countries": countries,
    })

def continents_detail(request, continent_id):
    continent = Continent.objects.get(id=continent_id)
    country_form = CountryForm()
    return render(request, 'continents/detail.html', {
        "continent": continent,
        "country_form": country_form 
    })

def add_country(request, continent_id):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            continent_name = request.POST.get('continent_name')
            new_country = form.save(commit=False)
            continent = get_object_or_404(Continent, id=continent_id, name=continent_name)
            new_country.continent = continent
            new_country.save()
            return redirect('detail', continent_id=continent_id)
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {
        'form': form
        })

def countries_index(request):
    countries=Country.objects.all()
    return render(request, 'countries/detail.html', {
        "countries": countries,
    })

def countries_detail(request, continent_id, country_id):
    country = Country.objects.get(id=country_id)
    city_form = CityForm()
    return render(request, 'countries/detail.html', {
        "country": country,
        "city_form": city_form,
        "continent_id": continent_id
    })

class CountryUpdate(UpdateView):
    model = Country 
    fields = ['name', 'image', "mapsURL",]
    template_name = 'countries/country_form.html'
    success_url = '/locations'

def add_city(request, country_id, continent_id):
    form = CityForm(request.POST)
    if form.is_valid():
        new_city = form.save(commit=False)
        new_city.country_id = country_id
        new_city.continent_id = continent_id
        new_city.save()
        city = new_city
        print(city.id)
    return redirect("countries_detail", country_id=country_id, continent_id=continent_id)

def cities_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html',{
     "cities": cities  
    } 
)

def city_detail(request, city_id):
   city = City.objects.get(id=city_id)
   return render(request, 'cities/detail.html',{
      "city": city,
   })

class CityUpdate(UpdateView):
   model = City 
   fields = ["name", "image", "mapsURL",]
   template_name = 'cities/city_form.html'
   success_url = '/locations'
   
class CityDelete(DeleteView):
   model = City
   success_url = "/locations"
   template_name = 'cities/city_confirm_delete.html'

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)