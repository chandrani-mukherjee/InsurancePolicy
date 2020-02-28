from rest_framework import serializers 
from .models import Customer 
 
 
class CustomerSerializers(serializers.ModelSerializer): 
     """ Serializer for Book """ 
 
 
     class Meta: 
         model = Customer 
         fields = ("id","First_Name","Last_Name","DOB")
