from django.conf.urls import patterns, include, url
from mysite.views import hello, my_homepage, current_datetime, hours_ahead
from books import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', my_homepage),
	url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^time/future/$', hours_ahead),
	url(r'^search/$', views.search),
	url(r'^contact/$', views.contact),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
