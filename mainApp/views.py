from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

#CRUD

#Read
class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

#Update
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

#Create
class CreateTodo(generics.CreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

#Delete
class DeleteTodo(generics.DestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer