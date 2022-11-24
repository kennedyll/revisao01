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