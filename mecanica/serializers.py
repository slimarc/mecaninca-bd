from rest_framework import serializers
from .models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico, Peca, PecaQuantidade, \
    OrdemDeCompra, Fornecedor


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = '__all__'


class AgendamentoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendamentoServico
        fields = '__all__'


class OrdemDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = '__all__'


class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca
        fields = '__all__'


class PecaQuantidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PecaQuantidade
        fields = '__all__'


class OrdemDeCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeCompra
        fields = '__all__'


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'