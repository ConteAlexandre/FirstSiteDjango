# This file, we permit to define the url with the method who correspond
from django.conf.urls import url
from . import views

# Define the patterns
urlpatterns = [

    # When tape the url without name after, we call this method, the method home who is define in the file views
    url(r'^$', views.home, name='home'),

    url(r'^about/$', views.about, name='about')
]
