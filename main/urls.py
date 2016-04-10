from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^contact_us/$', views.home, name='contact_us'),
	url(r'^about_us$', views.about_us, name='about_us'),
	url(r'^help/$', views.help, name='help'),
	url(r'^alert/$', views.create_alert, name='create_alert'),
	url(r'^register/$', views.register, name='register'),
	url(r'^handle_submission/$', views.handle_submission, name='handle_submission'),
]