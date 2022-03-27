from django.db import models
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE

from src.oauth.models import AuthUser


class Countries(models.Model):
    '''Countries tabels
    '''
    cout_id      = models.IntegerField(unique=True)
    cout_name_ru = models.CharField(max_length=100)
    cout_name_tj = models.CharField(max_length=100)
    cout_name_en = models.CharField(max_length=100)
    cout_avail   = models.BooleanField(default=True)

    def __str__(self):
        return self.cout_name_ru

class Cities(models.Model):
    '''Citites tables
    '''
    cout_cout_id = models.ForeignKey(Countries, on_delete=CASCADE)
    city_id      = models.IntegerField()
    city_name_ru = models.CharField(max_length=100)
    city_name_en = models.CharField(max_length=100)
    city_name_tj = models.CharField(max_length=100)
    city_avail   = models.BooleanField(default=True)

    def __str__(self):
        return self.city_name_ru

class Trips(models.Model):
    '''Model for trips
    '''
    trip_id      = models.BigAutoField(primary_key=True)#Autoincreameting field
    trip_date    = models.DateTimeField(auto_now=True)
    trip_owner   = models.ForeignKey(AuthUser, on_delete=CASCADE)
    trip_price   = models.DecimalField(max_digits=6, decimal_places=2)
    trips_desc   = models.TextField(max_length=1500)
    from_city    = models.ForeignKey(Cities, on_delete=CASCADE, related_name='from_city')
    to_city      = models.ForeignKey(Cities, on_delete=CASCADE, related_name='to_city')
    from_country = models.ForeignKey(Countries, on_delete=CASCADE, related_name='from_country')
    to_country   = models.ForeignKey(Countries, on_delete=CASCADE, related_name='to_country')

    def __str__(self):
        return str(self.trip_id)    
