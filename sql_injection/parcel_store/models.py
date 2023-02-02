from django.db import models


class ParcelStore(models.Model):

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    opening_hours = models.CharField(max_length=64)

    def __str__(self):
        return self.name
