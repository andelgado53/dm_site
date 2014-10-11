from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.db.models import get_model
from reporting.models import Categories, Tables
import tweet_stream
from django.template import RequestContext
from reporting.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request, template):

	category_list = Categories.objects.all()
	#return render_to_response('index.html', {'category_list': category_list})
	#locals() grabs all the varialbles and creates a dict 
	# if request.user.is_authenticated():
	# 	return render(request, template, locals())
	# else:
	# 	return redirect('login')
	
	# else:
	# 	user_name = None 
	# if 'test_id' not in request.session:
	# 	request.session['test_id'] = '123'
	# session_data = request.session['test_id']
	#print(request.user)
	#user_name = request.user

	context_instance=RequestContext(request)
	print(context_instance)
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
	#user_name = request.user
	if period == 'weekly':
		results = get_model('reporting', table_name).objects.filter(week__isnull=False)
	else:
		results = get_model('reporting', table_name).objects.filter(week__isnull=True)
	return render(request, template, locals() )
	
def twit_stream(request, template):
	
	#user_name = request.user
	twits = tweet_stream.get_twits(100, 'amazon prime music')
	list_of_twits = [(t['twit_text'].decode('utf-8') + ':\t\t\ttwitted by: '+ t['user']['user_name'] + '\t\t\t at: ' + t['date_created'], t['profile_pic'], "https://twitter.com/" + t['user']['user_name']) for t in twits]
	return render(request, template, locals())

	#{'list_of_twits': list_of_twits}

def log_in(request):
	
	errors = False
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('index')
		else:
			errors = True
	

	return render(request, 'login.html', locals())

def register(request):

	form = RegisterForm()
	if request.method == 'POST':
		user_form = RegisterForm(data = request.POST)
		if user_form.is_valid():
			new_user = user_form.save()
			new_user.set_password(new_user.password)
			new_user.save()
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			login(request,user)

			return redirect('index')
		else:
			print user_form.errors
			errors = user_form.errors
	else:
		return render(request, 'register.html', locals())

def log_out(request):
	logout(request)
	return redirect('index')

def boot_test(request):
	 return render(request, 'boot_test.html')


