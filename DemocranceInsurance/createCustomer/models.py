from django.db import models

# Create your models here.


class Customer(models.Model):
    # = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    DOB = models.CharField(max_length=30)
    