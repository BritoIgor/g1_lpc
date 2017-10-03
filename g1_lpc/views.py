from django.shortcuts import render
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from g1_lpc.models import *
from g1_lpc.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
