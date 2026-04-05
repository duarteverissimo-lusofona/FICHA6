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


# Representa um Trabalho Final de Curso
class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(blank=True)
    ano = models.IntegerField(blank=True, null=True)
    area_tematica = models.CharField(max_length=200)
    url_repositorio = models.URLField(blank=True, null=True)
    nivel_interesse = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    imagem = models.ImageField(upload_to='tfcs/', blank=True, null=True)

    def __str__(self):
        return self.titulo


# Representa uma competência
class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    categoria =  models.CharField(max_length=100, blank=True) 
    descricao = models.TextField(blank=True, null=True)
    nivel = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.nome


# Representa uma experiência profissional
class ExperienciaProfissional(models.Model):
    TIPO_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Estágio', 'Estágio'),
    ]

    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


# Representa o Making Of
class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    decisoes = models.TextField(blank=True, null=True)
    erros_correcoes = models.TextField(blank=True, null=True)
    data_registo = models.DateTimeField(auto_now_add=True)
    entidade_referida = models.CharField(max_length=200, blank=True)
    foto_papel = models.ImageField(upload_to='making_of/', blank=True, null=True)
    uso_ia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo