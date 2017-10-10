from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from g1_lpc.models import *
from django.conf.urls import url, include

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ('titulo', 'descricao')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome', 'email')

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    tipo = TipoSerializer(many=False)
    usuario = UsuarioSerializer(many=False)
    class Meta:
        model = Agenda
        fields = ('tipo', 'nome', 'usuario')

class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    agenda = AgendaSerializer(many=False)
    class Meta:
        model = Compromisso
        fields = ('nome', 'dataInicio', 'dataFim', 'agenda')

class CompromissoSimplesSerializer(serializers.HyperlinkedModelSerializer):
    agenda = AgendaSerializer(many=False)
    class Meta:
        model = Compromisso
        fields = ('id', 'nome')

class ConviteSerializer(serializers.HyperlinkedModelSerializer):
    convidado = UsuarioSerializer(many=False)
    compromisso = CompromissoSerializer(many=False)
    class Meta:
        model = Convite
        fields = ('msg', 'convidado', 'compromisso')
