from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def index(request):

	#return HttpResponse('this is the index of the DM reporting page')
	return render_to_response('index.html', )

def report_request(request, category):

	""" use the category to search table 'tables' for for tables under that category to display in drop down menu"""
	display_category = category.replace('_', ' ').title()
	return render_to_response('report.html', {'category_header' : display_category})