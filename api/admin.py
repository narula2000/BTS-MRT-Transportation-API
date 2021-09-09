from django.contrib import admin
from .models import Station, Train, Train_to_Station

admin.register(Station)
admin.register(Train)
admin.register(Train_to_Station)

