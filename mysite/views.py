from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
	return HttpResponse("Hello world")
	
def my_homepage(request):
	browser = request.META.get('HTTP_USER_AGENT', 'unknown')
	if browser == 'unknown':
		browser = False
	return render(request, 'myhomepage.html', {'browser': browser})
	
def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date':now})
	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	if offset > 1: 
		plural_hours=True
	else:
		plural_hours=False
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt, 'plural_hours': plural_hours})
	
def book_list(request):
	books = Book.objects.order_by('name')
	return render(request, 'book_list.html', {'books':books})