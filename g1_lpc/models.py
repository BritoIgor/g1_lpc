from django.db import models
from django.utils import timezone



class Usuario(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField('email')

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.CharField('descricao', null=True, max_length=300)

    def __str__(self):
        return self.titulo

class Compromisso(models.Model):
    nome = models.TextField('nome')
    dataInicio = models.DateTimeField('dataInicio')
    dataFim = models.DateTimeField('dataFim')
    agenda = models.ForeignKey('Agenda')

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    nome = models.TextField('nome')
    tipo = models.ForeignKey('Tipo')
    usuario = models.ForeignKey('Usuario')

    def __str__(self):
        return self.nome

class Convite(models.Model):
    msg = models.TextField('nome')
    convidado = models.ForeignKey('Usuario')
    Compromisso = models.ForeignKey('Compromisso')

    def __str__(self):
        return self.msg

##class Resposta_Convite(models.Model):
##    convidado = models.ForeignKey('Convite')
##    aceite = models.BooleanField('aceite')
