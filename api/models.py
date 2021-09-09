from django.db import models


class Station(models.Model):
    station_id = models.CharField(max_length=5, primary_key=True)
    station_name = models.CharField(max_length=40)

    def __str__(self):
        return "%s: %s" % (self.station_id, self.station_name)


class Station_Link(models.Model):
    start_station_id = models.CharField(max_length=5)
    end_station_id = models.CharField(max_length=5)

    def __str__(self):
        return "%s -> %s" % (self.start_station_id, self.end_station_id)
