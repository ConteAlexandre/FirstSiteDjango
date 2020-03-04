# This file, we permit to define the url with the method who correspond
from django.conf.urls import url
from . import views

# Define the patterns
urlpatterns = [

    url(r'^new/(?P<word>.*)/$', views.news_detail, name="news_detail")
]