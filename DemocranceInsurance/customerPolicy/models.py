from django.db import models

# Create your models here.

class Policy(models.Model):
    # = models.AutoField(primary_key=True)
    
    Type = models.CharField(max_length=30)
    Premium = models.CharField(max_length=30)
    Cover = models.IntegerField(max_length=30)
    