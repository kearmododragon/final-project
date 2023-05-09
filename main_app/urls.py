from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('holidays/', views.holidays, name='holidays'),
    path('locations/', views.locations_landing, name='landing'),
    path('locations/continents/', views.continents_index, name='index'),
    path('continents/<int:continent_id>/', views.continents_detail, name='detail'),
    path('locations/countries/', views.countries_index, name='index'),
    path('locations/cities/', views.cities_index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
]