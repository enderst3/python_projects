# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length = 200)
    location_type = models.CharField(max_length = 200)

    def __str__(self):
        return self.location_name

class Property(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    property_name = models.CharField(max_length = 200)
    area = models.CharField(max_length = 200)

    def __str__(self):
        return self.property_name