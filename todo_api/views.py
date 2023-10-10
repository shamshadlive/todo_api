from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for GET POST DELETE todos
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    http_method_names = ['get', 'post', 'head','delete']
    
    