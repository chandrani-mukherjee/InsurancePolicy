from django.shortcuts import render
import json
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from subprocess import Popen, PIPE
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializers

class createCustomer(APIView):
    permission_classes = (IsAuthenticated,)  
    serializer_class = CustomerSerializers
    
    def __init__(self):
        self.result_t1 = False
        
    def post(self,request):
       customer_obj = CustomerSerializers(data=request.data)
       
       if customer_obj.is_valid():
          print("Inside is valid")
          customer_obj.save()
       else:
          print(customer_obj.errors)
       print(customer_obj.data)
       
       return Response(customer_obj.data,status=status.HTTP_201_CREATED)        
