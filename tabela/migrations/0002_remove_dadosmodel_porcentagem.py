# Generated by Django 4.0.6 on 2022-07-13 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosmodel',
            name='porcentagem',
        ),
    ]
