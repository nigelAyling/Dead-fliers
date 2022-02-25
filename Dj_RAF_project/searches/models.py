from django.db import models

# Create your models here.
class Airmen(models.Model):
    surname = models.CharField(max_length=20)
    first_names = models.CharField(max_length=20)
    rank = models.CharField(max_length=20)
    service_number = models.CharField(max_length=20)
    date = models.DateField()
    age = models.IntegerField()
    unit = models.CharField(max_length=20)
    cemetery = models.CharField(max_length=20)
    aircraft = models.CharField(max_length=20)
    serial_no = models.CharField(max_length=10)
    base = models.CharField(max_length=20)
    circumstance = models.TextField()
