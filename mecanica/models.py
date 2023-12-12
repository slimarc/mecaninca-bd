from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    telefone = models.CharField(max_length=15, unique=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True, primary_key=True)
    modelo = models.CharField(max_length=20)
    ano_veiculo = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.placa


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Mecanico(models.Model):
    identificacao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.nome


def validador_data(valor):
    hoje = timezone.now().date()
    if valor < hoje:
        raise ValidationError('A data não pode ser anterior ao dia de hoje.')


class AgendamentoServico(models.Model):
    numero_agendamento = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data_previsao_entrada = models.DateField(validators=[validador_data])
    data_previsao_saida = models.DateField(validators=[validador_data])

    def __str__(self):
        return f"Agendamento #{self.numero_agendamento}"


class OrdemDeServico(models.Model):
    numero_ordem = models.AutoField(primary_key=True)
    servico = models.ManyToManyField(Servico)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data = models.DateField(validators=[validador_data])
    mecanico = models.ForeignKey(Mecanico, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f"Ordem #{self.numero_ordem}"


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True, primary_key=True)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome


class Peca(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome


class PecaQuantidade(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.peca} - {self.quantidade}"


class OrdemDeCompra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    peca_quantidades = models.ManyToManyField(PecaQuantidade)
    data_pedido = models.DateField(validators=[validador_data])
    data_entrega = models.DateField(validators=[validador_data])

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)

            for peca_quantidade in self.peca_quantidades.all():
                peca = peca_quantidade.peca
                quantidade = peca_quantidade.quantidade
                peca.estoque += quantidade
                peca.save()