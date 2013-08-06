from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.core.mail import send_mail
from books.forms import ContactForm

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Seriously? Dude, you can't search for nothing...that doesn't even make sense. Type something in that box, THEN press search.")
        elif len(q) > 20:
            errors.append("Whoa man, calm down. I can only handle 20 characters at a time.")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books':books, 'query':q})
    return render(request, 'search_form.html', {'errors': errors})

def contact(request):
	errors=[]
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','noreply@example.com'),
				['weskaplan95@gmail.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
	return render(request, 'contact_form.html', {'form': form})