# Generated by Django 3.1.5 on 2023-12-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0003_delete_historicomanutencao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='telefone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]