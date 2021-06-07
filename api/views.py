from functools import partial
from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets 
from rest_framework import viewsets 
from rest_framework.response import Response


class viewbook(viewsets.ViewSet):
    def list(self, request):
        
        stu = Book.objects.filter(status='Avaiable')
        serializer = BookSerializer(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        stu = Book.objects.filter(id=pk)
        serializer = BookSerializer(stu, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        if self.request.user.is_authenticated:
            stu = Book.objects.filter(id=pk)
            stu.delete()    
            return Response('Done!')
        
        return Response('Error: Please login first')


    def partial_update(self, request, pk=None):
        if self.request.user.is_authenticated:
            stu = Book.objects.get(id=pk)
            serializer = BookSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response('Data Updated')
        else:
            return Response('Error: Please login first')
        return Response(serializer.errors)


    

        
