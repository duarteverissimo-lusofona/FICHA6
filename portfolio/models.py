from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#Representa uma licenciatura
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    descricao = models.TextField(blank=True)
    objetivos = models.TextField(blank=True)
    ects_total = models.IntegerField(blank=True, null=True)
    duracao_anos = models.IntegerField(default=3)
    url_oficial = models.URLField(blank=True, null=True)
    departamento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

#Representa um Docente
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    url_pagina_lusofona = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)    

    def __str__(self):
        return self.nome


# Representa uma unidade curricular em abstrato
class UnidadeCurricular(models.Model):

    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20, blank=True)
    descricao = models.TextField(blank=True)
    ects = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)

    def __str__(self):
        return self.nome

#Representa uma Tecnologia
class Tecnologia(models.Model):

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_oficial = models.URLField(blank=True, null=True)
    nivel_interesse = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
        return self.nome


# Representa um projeto
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField(blank=True, null=True)
    url_github = models.URLField(blank=True, null=True)
    url_demo = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo