
from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
SALE_STATUS = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
        ('Reserved', 'Reserved'),
        ('Sold', 'Sold'),
    )
class Breed(models.Model):
    breed_name = models.CharField(max_length=200)
    

class Pet(models.Model):
    name = models.CharField(max_length= 200)
    age_days = models.IntegerField()
    breed = models.ForeignKey(Breed , related_name='breed', on_delete=models.CASCADE)
    color = models.CharField(max_length=200)
    status  = models.CharField(max_length=200 , choices=SALE_STATUS )
    description = models.TextField()
    
class Order(models.Model):
    product = models.ForeignKey(Pet , on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    
 

