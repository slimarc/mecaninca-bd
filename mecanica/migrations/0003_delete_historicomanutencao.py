# Generated by Django 3.1.5 on 2023-12-10 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0002_ordemdeservico_mecanico'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricoManutencao',
        ),
    ]