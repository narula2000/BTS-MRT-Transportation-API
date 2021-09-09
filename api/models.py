from django.db import models


class Station(models.Model):
    station_id = models.CharField(max_length=5, primary_key=True)
    station_name = models.CharField(max_length=40)

    def __str__(self):
        return "%s -> %s" % (self.station_id, self.station_name)
