# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . models import Warehouse, Items, Log

# Create your views here.

def add(request):
	if request.method=='POST':
		add_qty = request.POST['input_qty']
		location,item = request.POST['location'].split("_")
		warehouse_loc = Warehouse.objects.get(city=location)
		Item = Items.objects.get(warehouse_location=warehouse_loc.location_id,item_name=item)
		print add_qty
		Item.add_data(add_qty)
		Item.save()
		# log = Log.objects.create(item_name=item,qty=add_qty,location_to=warehouse_loc)
		# log.save()
	
	return index(request)


def move(request):
	if request.method=='POST':
		add_qty = request.POST['input_qty2']
		location,item = request.POST['location'].split("_")
		to_location = request.POST['to_location']
		warehouse_loc_from = Warehouse.objects.get(city=location)
		Item_from = Items.objects.get(warehouse_location=warehouse_loc_from.location_id,item_name=item)
		warehouse_loc_to = Warehouse.objects.get(city=to_location)
		#print "Moving ",Item_from.qty," ",Item_from.item_name," from ",warehouse_loc_from.city," to ",warehouse_loc_to.city
		Item_from.move_data(add_qty,warehouse_loc_to)
		
	return index(request)


def index(request):
	all_location = Warehouse.objects.all()
	loc_imgs = {}
	response = {}
	for loc in all_location:
		loc_items = Items.objects.all().filter(warehouse_location=loc)
		loc_imgs[loc.city]=str(loc.img_loc)
		items = []
		for i in loc_items:
			items.append({i.item_name:i.qty})
		response[loc.city] = items
	print loc_imgs['Kolkata']
	return render(request,"home.html",{'loc_cities':loc_imgs,'response':response})

def report(request):
	all_location = Warehouse.objects.all()
	response = {}
	for loc in all_location:
		loc_items = Items.objects.all().filter(warehouse_location=loc)
		items = []
		for i in loc_items:
			items.append({i.item_name:i.qty})
		response[loc.city] = items
	return render(request,"report.html",{'response':response})
