from rest_framework import serializers
from .models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico, HistoricoManutencao

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

class HistoricoManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoManutencao
        fields = '__all__'
