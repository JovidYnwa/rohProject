from django.contrib import admin
from . import models

@admin.register(models.Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('cout_name_ru', 'cout_name_tj','cout_name_en','cout_avail')


@admin.register(models.Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city_name_ru', 'city_name_en','city_name_tj','city_avail')

@admin.register(models.Trips)
class TripsAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 
    'trip_date',
    'trip_owner',
    'trip_price',
    'trips_desc',
    'from_city',
    'to_city',
    'from_country',
    'to_country')