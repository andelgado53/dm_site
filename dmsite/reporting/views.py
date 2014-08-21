from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.db.models import get_model
from reporting.models import Categories, Tables, prm_trcks_added

# Create your views here.

def index(request):

	category_list = Categories.objects.all()
	return render_to_response('index.html', {'category_list': category_list})

def report_request(request, category):
	""" use the category to search table 'tables' for for tables under that category to display in drop down menu"""
	
	tables = get_list_or_404(Tables, category= category)	
	display_category = category.replace('_', ' ').title()		
	return render_to_response('report.html', {'category_header' : display_category, 'tables': tables, 'category': category})

def display_results(request):

	#maper= {'weekly': week__isnull, 'monthly': month__isnull}
	table_name = request.GET['report']
	period = request.GET['period']
	table_desc = Tables.objects.get(name = table_name).description
	#table = get_model('reporting', table_name).objects.all()
	if period == 'weekly':
		table = get_model('reporting', table_name).objects.filter(week__isnull=False)
	else:
		table = get_model('reporting', table_name).objects.filter(week__isnull=True)
	return render(request, 'results.html', {'results': table, 'table_description': table_desc} )
	

def pop_table():

	data= {'year':2014, 'month':6, 'week':25, 'prm_trcks_added':150, 'customers': 15}
	a = prm_trcks_added(**data)
	a.save()

