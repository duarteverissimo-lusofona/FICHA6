from django.db import models

class Licenciatura(models.Model):


    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    descricao = models.TextField()
    objetivos = models.TextField()
    ects_total = models.IntegerField()
    duracao_anos = models.IntegerField()
    url_oficial = models.URLField()
    departamento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    url_pagina_lusofona = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)
    departamento = models.CharField(max_length=200)
    resumo = models.TextField(blank=True, null=True)       
    url_ciencia_vitae = models.URLField(blank=True, null=True)
    url_orcid = models.URLField(blank=True, null=True)       
    url_pure = models.URLField(blank=True, null=True)           
    
    def __str__(self):
        return self.nome
