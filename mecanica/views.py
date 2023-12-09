from rest_framework import viewsets, filters
from .models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico, HistoricoManutencao
from .serializers import ClienteSerializer, VeiculoSerializer, ServicoSerializer, MecanicoSerializer, AgendamentoServicoSerializer, OrdemDeServicoSerializer, HistoricoManutencaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['cpf', 'nome']
    filterset_fields = ['cpf']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['placa']
    filterset_fields = ['ano_veiculo', 'modelo']

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']

class MecanicoViewSet(viewsets.ModelViewSet):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['identificacao']
    filterset_fields = ['especialidade']

class AgendamentoServicoViewSet(viewsets.ModelViewSet):
    queryset = AgendamentoServico.objects.all()
    serializer_class = AgendamentoServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['numero_agendamento']
    filterset_fields = ['veiculo']

class OrdemDeServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['numero_ordem','mecanico']
    filterset_fields = ['veiculo','mecanico']

class HistoricoManutencaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoManutencao.objects.all()
    serializer_class = HistoricoManutencaoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['veiculo']

