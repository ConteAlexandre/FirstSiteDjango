# This file, we permit of define the different view with a method
from django.shortcuts import render, get_object_or_404, redirect

# Import the different models who utils
from main.models import Main
from .models import News


# Create your views here.

# Here, this method call the home file
def news_detail(request, word):

    site = Main.objects.get(pk=1)
    # Here we recover object main who is equal at pk number
    news = News.objects.filter(name=word)

    # We return the file html who correspond at the page who correspond with the name method
    return render(request, 'front/news_detail.html', {'news': news, 'site': site})

def news_list(request):

    # Here, we import the object news for listing in the view new_list
    news = News.objects.all()

    # We return the file html who correspond at the page who correspond with the name method
    return render(request, 'back/news_list.html', { 'news': news })

def news_add(request):

    # Condition for add the different input in the database, if this method equal as post
    if request.method == "POST":
        # Title
        newstitle = request.POST.get('newstitle')
        # Category
        newscat = request.POST.get('newscat')
        # Short text
        newstxtshort = request.POST.get("newstxtshort")
        # Body text
        newstxt = request.POST.get("newstxt")

    # Define a new page for add a new
    return render(request, 'back/news_add.html')