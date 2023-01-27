from dataclasses import fields
import email
from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    email = models.EmailField()
    data_nasc = models.DateField()
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)

class Agendamento (models.Model):

    FUNCIONARIO_CHOICES = [
    ("gregorio", "gregorio" ),
    ("jose", "jose"),
    ("gabriela", "gabriela"),
    ("laura", "laura"),
]

    SERVICO_CHOICES = [
    ("1 cabelo", "1 cabelo"),
    ("2 maquiagem", "2 maquiagem"),
    ("3 estetica","3 estetica"),
    ("4 manicure", "4 manicure"),
]

    TIME_CHOICES = [
    ("", ""),
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

    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    endereco = models.EmailField()
    funcionario = models.CharField(max_length=100, choices=FUNCIONARIO_CHOICES, blank=True, null=True)
    servico = models.CharField(max_length=100, choices=SERVICO_CHOICES, blank=True, null=True)
    data = models.DateField()
    horario = models.CharField(max_length=100, choices=TIME_CHOICES, blank=True, null=True)

class Servicos(models.Model):
    servico = models.CharField(max_length=120) 
    valor = models.IntegerField()
    preenchido = models.ManyToManyField(Agendamento, through='Servicos_preenchido')

class Servicos_preenchido(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)