# This file, we permit to define the model who can to be include in the panel admin
from django.contrib import admin
from .models import Main

# Register your models here.

# Here, we register the different model
admin.site.register(Main)
