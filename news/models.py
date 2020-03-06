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

    # The text with small description for the Home site
    short_txt = models.TextField()

    # All details of this news for the page details
    body_txt = models.TextField()

    # Date of created
    date = models.CharField(max_length=12)

    pic = models.TextField()

    # Who is writer
    writer = models.CharField(max_length=30)

    # Here we define what his display in the panel admin in the objects
    def __str__(self):
        return self.name + " | " + str(self.pk)

