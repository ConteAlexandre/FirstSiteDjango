# Here we define the Models
# This import is very important because he permit the migration
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# Created the class Main with attributes
class Main(models.Model):

    # Here we define the different attributes and their nature, different parameters
    # This name which appears with favicon
    name = models.CharField(max_length=30)

    # About
    about = models.TextField()

    # Facebook
    fb = models.CharField(default="-", max_length=30)

    # Twitter
    tw = models.CharField(default="-", max_length=30)

    # YouTube
    yt = models.CharField(default="-", max_length=30)

    # Phone
    tell = models.CharField(default="-", max_length=30)

    # Link for the team
    link = models.CharField(default="-", max_length=30)

    # This name define the title of this object when created
    set_name = models.CharField(default="-", max_length=30)

    # Here we define what his display in the panel admin in the objects
    def __str__(self):
        return self.set_name + " | " + str(self.pk)

