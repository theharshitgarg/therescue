from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.http import Http404
from django.shortcuts import render
import pygal
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
	print "HOME VIEW CALLED"
	template = loader.get_template('main/home.html')
	context = {
		#'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	#return HttpResponse("Hello World")

def contact_us(request):
	context = {}
	template = loader.get_template('main/Contact_us.html')
	return HttpResponse(template.render(context, request))

def about_us(request):
	return render(request, 'main/About_us.html', {})


def help(request):
	return HttpResponse("Help Section")

def create_alert(reqquest):
	return HttpResponse("Create Alert")

def handle_submission(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print request.POST
        print "-----"*3,request.POST.get('choice1')
        # form = NameForm(request.POST)
        # check whether it's valid:
        return render(request, 'main/home.html', {})

def register(request):
	if request.method == 'GET':
		print "REGISTER CALLED"
		context = {}
		template = loader.get_template('main/registration.html')
		return HttpResponse(template.render(context, request))
	else:
		print "POST REQUSET"
		print "THIS"
		print request.POST

		context = {}
		template = loader.get_template('main/registration.html')
		return HttpResponse(template.render(context, request))