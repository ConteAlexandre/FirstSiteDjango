# Here we define the Models
# This import is very important because he permit the migration
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Created the class Main with attributes
class News(models.Model):

    # Here we define the different attributes and their nature, different parameters
    # This name which appears with favicon
    name = models.CharField(max_length=50)

    # About
    short_txt = models.TextField()

    body_txt = models.TextField()

    date = models.CharField(max_length=12)

    pic = models.TextField()

    writer = models.CharField(max_length=30)

    # Here we define what his display in the panel admin in the objects
    def __str__(self):
        return self.name + " | " + str(self.pk)

