from django.http import HttpResponse
from django.shortcuts import render
import datetime
import httpagentparser

def hello(request):
	return HttpResponse("Hello world")
	
def my_homepage(request):
	data = request.META.get('HTTP_USER_AGENT', 'unknown')
	if data == 'unknown':
		data = False
	else:
		browser, os = httpagentparser.detect(data)['browser']['name'], httpagentparser.detect(data)['os']['name']
	return render(request, 'myhomepage.html', {'data':data, 'browser': browser, 'os':os})
	
def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date':now})
	
def hours_ahead(request, offset=None):
	errors = []
	if 'q' in request.GET:
		offset = request.GET['q']
		try:
			offset = int(offset)
			if offset == 0:
				errors.append("That's what clocks are for dummy!")
				dt = datetime.datetime.now()
				offset = '0'
			else:
				try:
					dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
				except OverflowError:
					offset, dt = None, None
					errors.append("Okay, that's too far. This time machine doesn't go that far into the future, deal with it.")
		except ValueError:
			offset, dt = None, None	
			errors.append("Listen buddy, don't make this hard on yourself. Just enter an integer so we can go to the future")
		if offset and offset > 1 or offset < -1: 
			plural_hours=True
		else:
			plural_hours=False
		return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt, 'plural_hours': plural_hours, 'errors' : errors})
	else:
		return render(request, 'hours_ahead.html', {'hour_offset': None, 'next_time': None, 'plural_hours': None, 'errors' : errors})

def book_list(request):
	books = Book.objects.order_by('name')
	return render(request, 'book_list.html', {'books':books})
	