from django.db import models

# Create your models here.
class Airmen(models.Model):
    surname = models.CharField(max_length=200)
    first_names = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    service_number = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    age = models.IntegerField()
    unit = models.CharField(max_length=200)
    cemetery = models.CharField(max_length=200)
    aircraft = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    circumstance = models.TextField()
