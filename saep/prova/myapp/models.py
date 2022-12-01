from dataclasses import fields
import email
from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    sobrenome = models.CharField(max_length=16)
    telefone = models.CharField(max_length=16)

class Agendamento (models.Model):

    FUNCIONARIO_CHOICES = [
    ("gregorio", "gregorio" ),
    ("jose", "jose"),
    ("gabriela", "gabriela"),
    ("laura", "laura"),
]

    SERVICO_CHOICES = [
    ("1 people", "1 people"),
    ("2 people", "2 people"),
    ("3 people","3 people"),
    ("4 people", "4 people"),
]

    TIME_CHOICES = [
    ("08:00 às 09:00", "08:00 às 09:00"),
    ("09:00 às 10:00", "09:00 às 10:00"),
    ("10:00 às 11:00", "10:00 às 11:00"),
    ("11:00 às 12:00", "11:00 às 12:00"),
    ("13:00 às 14:00", "13:00 às 14:00"),
    ("14:00 às 15:00", "14:00 às 15:00"),
    ("15:00 às 16:00", "15:00 às 16:00"),
    ("16:00 às 17:00", "16:00 às 17:00"),
    ("17:00 às 18:00", "17:00 às 18:00"),
    ("18:00 às 19:00", "18:00 às 19:00"),
]

    nome_completo = models.CharField(max_length=255)
    numero_de_telefone = models.CharField(max_length=30)
    endereco = models.EmailField()
    selecione_o_funcionario = models.CharField(max_length=100, choices=FUNCIONARIO_CHOICES, blank=True, null=True)
    selecione_o_sevico = models.CharField(max_length=100, choices=SERVICO_CHOICES, blank=True, null=True)
    data_de_agendamento = models.DateField()
    horario = models.CharField(max_length=100, choices=TIME_CHOICES, blank=True, null=True)




class Servicos(models.Model):
    servico = models.CharField(max_length=120) 
    valor = models.IntegerField()
    preenchido = models.ManyToManyField(Agendamento, through='Servicos_preenchido')

class Servicos_preenchido(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)