# This file, we permit of define the different view with a method
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Main
from .models import News


# Create your views here.

# Here, this method call the home file
def news_detail(request, word):

    site = Main.objects.get(pk=1)
    # Here we recover object main who is equal at pk number
    news = News.objects.filter(name=word)

    # We return the file html who correspond at the home
    return render(request, 'front/news_detail.html', {'news': news, 'site': site})

def news_list(request):


    return render(request, 'back/news_list.html')