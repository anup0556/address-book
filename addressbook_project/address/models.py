# addressbook/models.py
from django.db import models

class Address(models.Model):
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=50)  

    def __str__(self):
        return self.address_line
