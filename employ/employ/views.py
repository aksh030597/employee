from curses.ascii import EM
import re
from urllib import response
from urllib import request
from urllib.request import Request
from django.http import JsonResponse
from .models import Emp
from .serializers import Empserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from employ import serializers


@api_view(['GET', 'POST'])
def emp_list(request):
    if request.method == 'GET':
        emp = Emp.objects.all() 
        serializer = Empserializers(emp, many=True)
        return Response({'emp': serializer.data})

    if request.method == 'POST':
        serializer = Empserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "record added successfully!!!")
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def emp_detail(request, id):

    try:
        emp= Emp.objects.get(pk=id)
    except Emp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = Empserializers(emp)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = Empserializers(emp, data=request.data)
    
        if serializers.is_valid()==True:
            serializers.save()
            messages.success(request, "record added successfully!!!")
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method=='DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






