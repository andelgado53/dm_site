from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.db.models import get_model
from reporting.models import Categories, Tables
import tweet_stream


# Create your views here.

def index(request, template):

	category_list = Categories.objects.all()
	#return render_to_response('index.html', {'category_list': category_list})
	return render(request, template, {'category_list': category_list, 'page_title': page_title})

def report_request(request, category, template):
	""" use the category to search table 'tables' for for tables under that category to display in drop down menu"""
	
	tables = get_list_or_404(Tables, category= category)	
	display_category = category.replace('_', ' ').title()	
	return render(request, template, {'category_header' : display_category, 'tables': tables, 'category': category})

def display_results(request, template):

	table_name = request.GET['report']
	period = request.GET['period']
	table_desc = Tables.objects.get(name = table_name).description
	if period == 'weekly':
		table = get_model('reporting', table_name).objects.filter(week__isnull=False)
	else:
		table = get_model('reporting', table_name).objects.filter(week__isnull=True)
	return render(request, template, {'results': table, 'table_description': table_desc} )
	
def twit_stream(request, template):
	
	twits = tweet_stream.get_twits(100, 'amazon prime music')
	list_of_twits = [t['twit_text'].decode('utf-8') + ':\t\t\ttwitted by: '+ t['user']['user_name'] + '\t\t\t at: ' + t['date_created'] for t in twits]
	return render(request, template, {'list_of_twits': list_of_twits})



