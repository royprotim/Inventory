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

	def add_data(self,add_qty):
		self.qty = self.qty + int(add_qty)
		log = Log.objects.create(item_name=self.item_name,qty=int(add_qty),location_to=self.warehouse_location)
		log.save()

	def move_data(self,add_qty, warehouse_loc_to):
		self.qty = self.qty-int(add_qty)
		#print "Moving ",Item_from.qty," ",Item_from.item_name," from ",warehouse_loc_from.city," to ",warehouse_loc_to.city
		self.save()
					# Item_to = Items.objects.get(warehouse_location=warehouse_loc.location_id,item_name=item)
		if Items.objects.filter(warehouse_location=warehouse_loc_to.location_id,item_name=self.item_name).exists():
			Item_to = Items.objects.get(warehouse_location=warehouse_loc_to.location_id,item_name=self.item_name)
			
			Item_to.add_data(add_qty)
			Item_to.save()
			log = Log.objects.create(item_name=self.item_name,qty=add_qty,location_from=self.warehouse_location,location_to=warehouse_loc_to)
			log.save()
		else:
			Item_to = Items.objects.create(item_name=self.item_name,qty=add_qty,warehouse_location=warehouse_loc_to)
			Item_to.save()
			log = Log.objects.create(item_name=self.item_name,qty=add_qty,location_from=self.warehouse_location,location_to=warehouse_loc_to)
			log.save()

	def __unicode__(self):
		return self.item_name

class Log(models.Model):
	log_id = models.AutoField(primary_key=True)
	location_from = models.ForeignKey(Warehouse,on_delete=models.CASCADE,null=True,related_name='requests_from')
	location_to = models.ForeignKey(Warehouse,on_delete=models.CASCADE,related_name='requests_to')
	item_name = models.CharField(max_length=50)
	qty = models.IntegerField()
	time = models.DateTimeField(auto_now=True)