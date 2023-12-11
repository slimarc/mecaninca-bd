from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from .models import Cliente, Veiculo, Servico, Mecanico, AgendamentoServico, OrdemDeServico
from .serializers import ClienteSerializer, VeiculoSerializer, ServicoSerializer, MecanicoSerializer, AgendamentoServicoSerializer, OrdemDeServicoSerializer
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

    def veiculos_por_cliente(self, cpf):
        cliente = get_object_or_404(Cliente, cpf=cpf)
        veiculos = Veiculo.objects.filter(cliente=cliente)
        veiculos_json = [{
            'placa': veiculo.placa if veiculo.placa else None,
            'modelo': veiculo.modelo if veiculo.modelo else None,
            'ano_veiculo': veiculo.ano_veiculo if veiculo.ano_veiculo else None
        }
            for veiculo in veiculos]
        return JsonResponse({'cliente': cliente.nome, 'veiculos': veiculos_json})


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['placa']
    filterset_fields = ['ano_veiculo', 'modelo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MecanicoViewSet(viewsets.ModelViewSet):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['identificacao']
    filterset_fields = ['especialidade']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AgendamentoServicoViewSet(viewsets.ModelViewSet):
    queryset = AgendamentoServico.objects.all()
    serializer_class = AgendamentoServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['numero_agendamento']
    filterset_fields = ['veiculo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class OrdemDeServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['numero_ordem','mecanico']
    filterset_fields = ['veiculo','mecanico']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


def historico_do_veiculo(request, placa):
    veiculo = get_object_or_404(Veiculo, placa=placa)
    ordens = OrdemDeServico.objects.filter(veiculo=veiculo)
    ordens_json = [{
                    'numero_ordem': ordem.numero_ordem if ordem.numero_ordem else None,
                    'data': ordem.data if ordem.data else None,
                    'veiculo': ordem.veiculo.placa if ordem.veiculo else None,
                    'mecanico': ordem.mecanico.nome if ordem.mecanico else None,
                    "servico": [
                        {
                            'nome': servico.nome if servico.nome else None,
                            'descricao': servico.descricao if servico.descricao else None,
                            'valor': float(servico.valor) if servico.valor else None
                        } for servico in ordem.servico.all()
                    ]
                   } for ordem in ordens]
    return JsonResponse({'veiculo': veiculo.placa, 'ordens': ordens_json})