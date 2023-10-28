from django.utils.timezone import now
from django.contrib.gis.db import models

from django.contrib.gis.geos import WKTReader, MultiPolygon


class SatellitePictureModel(models.Model):
    link = models.CharField(max_length=256, null=True, blank=True)
    lat_1 = models.FloatField(null=True)
    lon_1 = models.FloatField(null=True)
    lat_2 = models.FloatField(null=True)
    lon_2 = models.FloatField(null=True)
    polygon = models.MultiPolygonField(srid=4326, null=True)
    created_at = models.DateTimeField(default=now)
    expiration_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if all((getattr(self, attr) for attr in ("lat_1", "lat_2", "lon_1", "lon_2"))):
            """self.polygon = MultiPolygon("POLYGON (({} {}, {} {}, {} {}, {} {}, {} {}))".format((self.lat_1, self.lon_1, self.lat_2, self.lon_1,
                                      (self.lat_2, self.lon_2), (self.lat_1, self.lon_2), (self.lat_1, self.lon_1))
                                        ")"))"""
        super(SatellitePictureModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{str(self.link)}'


class PictureModel(models.Model):
    url = models.ImageField(max_length=256, upload_to='pictures/', null=True, blank=True)
    link = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{str(self.url)}'
