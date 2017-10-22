# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recharge
from .serializers import RechargeSerializer

# Create your views here.
class RechargeList(APIView):

       def get(self,request):
           user=self.request.GET['user']
           mobile_number=self.request.GET['mobile_number']
           recharge_amount=self.request.GET['recharge_amount']
           Recharge1=Recharge.objects.filter(first_name=user)
           serializer = RechargeSerializer(Recharge1, many=True)

           if (len(Recharge1) > 0):
               result = serializer.data[0]["account_balance"] - int(recharge_amount)
               if (serializer.data[0]["account_balance"] < int(recharge_amount)):
                   return Response("Not Sufficient Balance")
               else:
                   return Response(
                       "Recharge Successful And Your Remaining Account Balance in your wallet is" + " Rs " + str(result))

           else:
               return Response("No User with This First Name ! Please type correct First Name")


def rechargeView(request):
    data=Recharge.objects.all()
    context={'data':data}
    return render(request,'recharge.html',context)



class UserCreate(CreateView):
    model=Recharge
    fields=['first_name','last_name','account_balance']
