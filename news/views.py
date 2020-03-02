# This file, we permit of define the different view with a method
from django.shortcuts import render, get_object_or_404, redirect
from .models import News

# Create your views here.

# Here, this method call the home file
def news_detail(request, pk):

    # Here we recover object main who is equal at pk number
    news = News.objects.filter(pk=pk)

    # We return the file html who correspond at the home
    return render(request, 'front/news_detail.html', {'news': news})
