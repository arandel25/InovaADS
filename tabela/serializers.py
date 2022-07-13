from dataclasses import fields
from pydoc import classname
from pyexpat import model
from rest_framework import serializers
from tabela.models import DadosModel

class TabelaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DadosModel
        exclude = ('modified', 'created',)