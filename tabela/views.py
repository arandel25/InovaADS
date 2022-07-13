from django.shortcuts import render
from .models import DadosModel

def home(request):
    gastos = DadosModel.objects.filter(tipo='fixo')
    return render(request, 'home.html', context={"gastos":gastos})

def variavel(request):
    gastos = DadosModel.objects.filter(tipo='variavel')
    return render(request, 'variavel.html', context={"gastos":gastos})

def funcionario(request):
    gastos = DadosModel.objects.filter(tipo='funcionario')
    return render(request, 'funcionario.html', context={"gastos":gastos})

def taxas(request):
    gastos = DadosModel.objects.filter(tipo='taxa')
    return render(request, 'taxas.html', context={"gastos":gastos})

def horas(request):
    return render(request, 'taxas.html')