from django.shortcuts import render
import json
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from subprocess import Popen, PIPE
from rest_framework import status
from .models import Policy
from .serializers import PolicySerializers

class createPolicy(APIView):
    permission_classes = (IsAuthenticated,)  
    serializer_class = PolicySerializers
    
    def __init__(self):
        self.result_t1 = False
        
    def post(self,request):
       policy_obj = PolicySerializers(data=request.data)
       
       if policy_obj.is_valid():
          print("Inside is valid")
          policy_obj.save()
       else:
          print(policy_obj.errors)
       print(policy_obj.data)
       
       return Response(policy_obj.data,status=status.HTTP_201_CREATED)        
