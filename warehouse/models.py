# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Warehouse(models.Model):
	location_id = models.AutoField(primary_key=True)
	city = models.CharField(max_length=50)
	img_loc = models.CharField(max_length=50,default='null')
	def __unicode__(self):
		return self.city


class Items(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_name = models.CharField(max_length=50)
	qty = models.IntegerField()
	warehouse_location = models.ForeignKey(Warehouse,on_delete=models.CASCADE)
	def __unicode__(self):
		return self.item_name