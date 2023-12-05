from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True, null=True)

class Consulta(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_consulta = models.DateField()