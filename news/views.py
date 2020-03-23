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

        # Validation Form
        if newstitle == "" or newstxt == "" or newstxtshort == "" or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', { 'error': error })

        # Here, we define the new object News and add the variables
        b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date="2020", pic="-", writer="-", catname=newscat, catid=0, show=0)

        # We call the method for recover the object
        b.save()

        # And redirect to the panel list news
        return redirect('news_list')

    # Define a new page for add a new
    return render(request, 'back/news_add.html')