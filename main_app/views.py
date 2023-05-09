from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

continents = [
   {"name": "Africa", "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Africa_%28orthographic_projection%29.svg/640px-Africa_%28orthographic_projection%29.svg.png" },
   {"name": "Asia", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Asia_%28orthographic_projection%29.svg/1200px-Asia_%28orthographic_projection%29.svg.png"},
   {"name": "Europe", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg/1200px-Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg.png"},
   {"name": "Oceana", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Oceania_%28centered_orthographic_projection%29.svg/1200px-Oceania_%28centered_orthographic_projection%29.svg.png"},
   {"name": "North America", "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Location_North_America.svg/1200px-Location_North_America.svg.png"},
   {"name": "South America", "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/South_America_%28orthographic_projection%29.svg/1200px-South_America_%28orthographic_projection%29.svg.png"},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def holidays(request):
    return render(request, 'holidays.html')

def locations_landing(request):
   return render (request, "locations/landing.html")

def continents_index(request):
    return render(request, 'continents/index.html',{
     "continents": continents  
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
