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
	#locals() grabs all the varialbles and creates a dict 
	return render(request, template, locals())

def report_request(request, category, template):
	""" use the category to search table 'tables' for for tables under that category to display in drop down menu"""
	
	category = category
	tables = get_list_or_404(Tables, category= category)	
	category_header = category.replace('_', ' ').title()	
	return render(request, template, locals())

def display_results(request, template):
	
	table_name = request.GET['report']
	period = request.GET['period']
	table_description = Tables.objects.get(name = table_name).description
	if period == 'weekly':
		results = get_model('reporting', table_name).objects.filter(week__isnull=False)
	else:
		results = get_model('reporting', table_name).objects.filter(week__isnull=True)
	return render(request, template, locals() )
	
def twit_stream(request, template):
	
	twits = tweet_stream.get_twits(100, 'amazon prime music')
	list_of_twits = [t['twit_text'].decode('utf-8') + ':\t\t\ttwitted by: '+ t['user']['user_name'] + '\t\t\t at: ' + t['date_created'] for t in twits]
	return render(request, template, locals())

	#{'list_of_twits': list_of_twits}

