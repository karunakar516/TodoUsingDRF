from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
class TodoViewSet(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
