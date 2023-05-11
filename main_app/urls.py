from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('holidays/', views.holidays_index, name='holidays'),
    path('holidays/<int:holiday_id>/add_holiday',views.add_holiday, name="add_holiday" ),
    path('holiday/<int:holiday_id>/', views.holiday_detail, name="holiday_detail"),

    path('events/', views.events_index, name="events-index"),
    path('events/<int:event_id>/', views.event_detail, name="event-detail"),

    path('locations/', views.locations_landing, name='landing'),
    
    path('locations/continents/', views.continents_index, name='index'),
    path('locations/<int:continent_id>/', views.continents_detail, name='detail'),

    path('locations/<int:continent_id>/add_country/', views.add_country, name='add_country'),
    path('locations/<int:continent_id>/<int:country_id>/', views.countries_detail, name='countries_detail'),
    path('countries/<int:country_id/update/', views.CountryUpdate.as_view(), name ="country_update"),
    path('countries/<int:country_id/delete/', views.CountryDelete.as_view(), name ="country_delete"),

    path('locations/<int:continent_id>/<int:country_id>/add_city/', views.add_city, name='add_city'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name="cities_update"),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name="cities_delete"),

    path('cities/', views.cities_index, name='index'),

    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
]