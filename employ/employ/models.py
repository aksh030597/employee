from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models


class Emp(models.Model):
    name= models.CharField(max_length=200)
    desc= models.CharField(max_length=200)


    def __str__(self):

        return self.name+" "+self.desc




