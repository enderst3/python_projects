# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Property, Location
from django.contrib import admin

# Register your models here.

admin.site.register(Property)
admin.site.register(Location)
