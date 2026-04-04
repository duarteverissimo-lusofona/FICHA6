from django.db import models

class Licenciatura(models.Model):
    GRAU_CHOICES = [
        ('LIC', 'Licenciatura'),
        ('PG', 'Pós-Graduação'),
        ('MST', 'Mestrado'),
        ('DOT', 'Doutoramento'),
    ]

    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    grau = models.CharField(max_length=50, choices=GRAU_CHOICES)
    descricao = models.TextField()
    objetivos = models.TextField()
    ects_total = models.IntegerField()
    duracao_anos = models.IntegerField()
    url_oficial = models.URLField()
    departamento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
