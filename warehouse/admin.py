# -*- coding: utf-8 -*-
from django.contrib import admin

from . models import Warehouse, Items, Log

admin.site.register(Warehouse)
admin.site.register(Items)
admin.site.register(Log)
# Register your models here.
