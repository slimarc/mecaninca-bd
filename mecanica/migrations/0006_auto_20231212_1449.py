# Generated by Django 3.1.5 on 2023-12-12 17:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mecanica.models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0005_auto_20231211_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True)),
                ('cep', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='agendamentoservico',
            name='data_previsao_entrada',
            field=models.DateField(validators=[mecanica.models.validador_data]),
        ),
        migrations.AlterField(
            model_name='agendamentoservico',
            name='data_previsao_saida',
            field=models.DateField(validators=[mecanica.models.validador_data]),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='data',
            field=models.DateField(validators=[mecanica.models.validador_data]),
        ),
        migrations.CreateModel(
            name='PecaQuantidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('peca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mecanica.peca')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField(validators=[mecanica.models.validador_data])),
                ('data_entrega', models.DateField(validators=[mecanica.models.validador_data])),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mecanica.fornecedor')),
                ('peca_quantidades', models.ManyToManyField(to='mecanica.PecaQuantidade')),
            ],
        ),
    ]
