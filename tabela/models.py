from pyexpat import model
from django.db import models

class DadosModel(models.Model):
    
    nome = models.CharField(
        max_length=100
    )
    
    valor = models.FloatField(
        max_length=14
    )
    
    tipo = models.CharField(
        max_length=100
    )
    
    def __str__(self) -> str:
        return f"{self.nome}"