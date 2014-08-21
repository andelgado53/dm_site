from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import get_model
from reporting.models import Categories, Tables, prm_trcks_added

# Create your views here.

def index(request):

	category_list = Categories.objects.all()

	return render_to_response('index.html', {'category_list': category_list})

def report_request(request, category):

	""" use the category to search table 'tables' for for tables under that category to display in drop down menu"""
	tables = Tables.objects.filter(category= category)
	
	display_category = category.replace('_', ' ').title()
		
	return render_to_response('report.html', {'category_header' : display_category, 'tables': tables})

def display_results(request):

	table_name = request.GET['report']
	table = get_model('reporting', table_name).objects.all()
	return render(request, 'test.html', {'results': table} )
	#return render_to_response('results.html',{'results': table})

	