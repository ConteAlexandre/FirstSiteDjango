# This file, we permit to define the url with the method who correspond
from django.conf.urls import url
from . import views

# Define the patterns
urlpatterns = [

    # Define the url for the news_detail
    url(r'^new/(?P<word>.*)/$', views.news_detail, name="news_detail"),

    # The url for listing the news in the panel
    url(r'^panel/news/list/$', views.news_list, name="news_list"),

    # The url for added the news in the panel
    url(r'^panel/news/add/$', views.news_add, name="news_add")
]