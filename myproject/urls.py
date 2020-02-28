from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Here, we define the waves who content the pattern admin in the url are contained in only line
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
]
