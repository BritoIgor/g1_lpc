# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(verbose_name='nome')),
                ('institucional', models.BooleanField(verbose_name='institucional')),
            ],
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(verbose_name='nome')),
                ('dataInicio', models.DateTimeField(verbose_name='dataInicio')),
                ('dataFim', models.DateTimeField(verbose_name='dataFim')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g1_lpc.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('descricao', models.CharField(max_length=300, null=True, verbose_name='descricao')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g1_lpc.Pessoa'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g1_lpc.Tipo'),
        ),
    ]
