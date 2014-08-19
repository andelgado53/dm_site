from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from reporting.models import Categories, Tables

# Create your views here.

def index(request):

	#return HttpResponse('this is the index of the DM reporting page')
	# category_list = [
	# 					'Prime', 
	# 					'Store',
	# 				 	'Library', 
	# 				 	'ClickStream',
	# 				  	'TwitterStream'
	# 				 ] # this will be replaced for a query to the categories table
	category_list = Categories.objects.all()

	return render_to_response('index.html', {'category_list': category_list})

def report_request(request, category):

	""" use the category to search table 'tables' for for tables under that category to display in drop down menu"""
	tables = Tables.objects.filter(category= category)
	
	display_category = category.replace('_', ' ').title()
		
	return render_to_response('report.html', {'category_header' : display_category, 'tables': tables})