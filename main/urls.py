# This file, we permit to define the url with the method who correspond
from django.conf.urls import url
from . import views

# Define the patterns
urlpatterns = [

    # When tape the url without name after, we call this method, the method home who is define in the file views
    url(r'^$', views.home, name='home'),

    # Define the wave for redirection the page about
    url(r'^about/$', views.about, name='about'),

    # Define the redirection with the wave panel
    url(r'^panel/$', views.panel, name='panel'),
]
