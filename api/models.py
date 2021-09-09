from django.db import models


class Train_to_Station(models.Model):
    station_id = models.CharField(max_length=5)
    train_id = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return "%s %s" % (self.station_id, self.train_id)


class Station(models.Model):
    station_id = models.CharField(max_length=5, primary_key=True)
    station_name = models.CharField(max_length=40)

    def __str__(self):
        return "%s -> %s" % (self.station_id, self.station_name)


class Train(models.Model):
    train_id = models.CharField(max_length=5, primary_key=True)
    start_station_id = models.CharField(max_length=5)
    end_station_id = models.CharField(max_length=5)

    def __str__(self):
        return "%s: %s -> %s" % (self.train_id, self.start_station_id, self.end_station_id)
