from django.db.models import fields
from rest_framework import serializers
from .models import Station, Train, Train_to_Station


class StationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class TrainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


class Train_to_StationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Train_to_Station
        fields = '__all__'
