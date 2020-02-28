# Here we define the Models
# This import is very important because he permit the migration
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Created the class Main with attributes
class Main(models.Model):

    # Here we define the different attributes and their nature
    name = models.TextField()

    # Define what attribute is a string
    def __str__(self):
        return self.name
