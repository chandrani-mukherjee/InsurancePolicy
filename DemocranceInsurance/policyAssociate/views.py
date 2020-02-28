from django.shortcuts import render
import json
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from subprocess import Popen, PIPE
from rest_framework import status
from .models import PolicyAssociate
from .serializers import PolicyAssociateSerializers
from createCustomer.models import Customer
from customerPolicy.models import Policy

class PolicyAssociate(APIView):
    permission_classes = (IsAuthenticated,)  
    serializer_class = PolicyAssociateSerializers

        
    def post(self,request):
       policy_associate_obj = PolicyAssociateSerializers(data=request.data)
       policy_reference  =  Policy.objects.filter(id=request.data['PolicyId'])
       print(policy_reference)
       customer_ref = Customer.objects.filter(id=request.data['CustId'])
       print(customer_ref)
       if policy_associate_obj.is_valid():
          print("Inside is valid")
          policy_associate_obj.save()
       else:
          print(policy_associate_obj.errors)
       print(policy_associate_obj.data)
       
       return Response(policy_associate_obj.data,status=status.HTTP_201_CREATED)        
