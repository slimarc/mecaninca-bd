from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    telefone = models.CharField(max_length=14, unique=True)
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
    telefone = models.CharField(max_length=14, unique=True)
    
    def __str__(self):
        return self.nome

class AgendamentoServico(models.Model):
    numero_agendamento = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data_agendamento = models.DateField()
    data_previsao = models.DateField()

    def __str__(self):
        return f"Agendamento #{self.numero_agendamento}"

class OrdemDeServico(models.Model):
    numero_ordem = models.AutoField(primary_key=True)
    servico = models.ManyToManyField(Servico)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data = models.DateField()
    mecanico = models.ForeignKey(Mecanico, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f"Ordem #{self.numero_ordem}"

class HistoricoManutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    ordem_de_servico = models.ManyToManyField(OrdemDeServico)

    