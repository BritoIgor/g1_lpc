from django.shortcuts import render
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from g1_lpc.models import *
from django.contrib.auth.models import User
from g1_lpc.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer
