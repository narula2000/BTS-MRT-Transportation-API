from django.contrib import admin
from .models import Station, Train, Train_to_Station

admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Train_to_Station)

