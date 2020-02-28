from rest_framework import serializers 
from .models import Policy 
 
 
class PolicySerializers(serializers.ModelSerializer): 
     """ Serializer for Book """ 
 
 
     class Meta: 
         model = Policy 
         fields = ("id","Type","Premium","Cover")
