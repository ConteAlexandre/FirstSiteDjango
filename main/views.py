# This file, we permit of define the different view with a method
from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


# Create your views here.

# Here, this method call the home file
def home(request):
    # We return the file html who correspond at the home
    return render(request, 'front/home.html')

def about(request):

    return render(request, 'front/about.html')
