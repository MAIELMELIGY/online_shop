from django.contrib import admin

# Register your models here.
from .models import Breed , Pet , Order
admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(Order)