# This file, we permit of define the different view with a method
from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News


# Create your views here.

# Here, this method call the home file
def home(request):

    # Here we recover object main who is equal at pk number
    site = Main.objects.get(pk=1)
    news = News.objects.all()

    # We return the file html who correspond at the home
    return render(request, 'front/home.html', {'site': site, 'news': news})

# Here, this method call the about file
def about(request):

    # Here we recover object main who is equal at pk number
    site = Main.objects.get(pk=1)

    # Return the file for the page about and define a parameter for recover the parameter
    return render(request, 'front/about.html', {'site': site})

# Here, it's a method for define the home page for panel
def panel(request):


    # We return the homepage
    return render(request, 'back/home.html')
